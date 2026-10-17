#!/usr/bin/env python3
"""Generate and verify complete family2 fibres at both quadratic exceptions.

All coefficient reduction and identity verification use only Python's
standard library. Rational source expressions are parsed with a restricted
AST evaluator and rederived during every verification. Macaulay2 is used
only to find complete polynomial duals, which this script independently checks.
"""
from fractions import Fraction as Q
from pathlib import Path
import ast
import hashlib
import itertools
import json
import math
import sys

HERE = Path(__file__).resolve().parent
CASES = {
    'qplus': {'modulus': 'k^2+1', 'relation': (Q(-1), Q(0)), 'discriminant': -4},
    'qminus': {'modulus': 'k^2-2*k-1', 'relation': (Q(1), Q(2)), 'discriminant': 8}
}
ZERO, ONE = (Q(0), Q(0)), (Q(1), Q(0))
SOURCE_INPUTS = ['localcoh-incidence-tensor.txt', 'localcoh-incidence-bases.txt',
                 'localcoh-symbol-top.json', 'session-localcoh-origin-family-2-seed.json']


class Audit:
    def __init__(self, case):
        self.case = case
        self.info = CASES[case]
        self.relation = self.info['relation']
        self.stem = 'session-localcoh-origin-family-2-exception-'+case
        self.cert = HERE/('session_localcoh_family2_'+case+'_audit_2026_10_08.json')

    def ftimes(self, a, b):
        c, d = self.relation
        return (a[0]*b[0]+c*a[1]*b[1],
                a[0]*b[1]+a[1]*b[0]+d*a[1]*b[1])

    def finverse(self, a):
        c, d = self.relation
        norm = a[0]**2+d*a[0]*a[1]-c*a[1]**2
        assert norm != 0, 'Source denominator is not a field unit'
        return ((a[0]+d*a[1])/norm, -a[1]/norm)

    @staticmethod
    def add(a, b):
        result = dict(a)
        for degree, coefficient in b.items():
            x = result.get(degree, ZERO)
            value = (x[0]+coefficient[0], x[1]+coefficient[1])
            if value == ZERO:
                result.pop(degree, None)
            else:
                result[degree] = value
        return result

    @staticmethod
    def scale(a, c):
        return {degree: (v[0]*c, v[1]*c) for degree, v in a.items() if c and v != ZERO}

    def multiply(self, a, b):
        result = {}
        for i, x in a.items():
            for j, y in b.items():
                value = self.ftimes(x, y)
                if value != ZERO:
                    result = self.add(result, {i+j: value})
        return result

    def power(self, value, exponent):
        assert exponent >= 0
        answer = {0: ONE}
        while exponent:
            if exponent & 1:
                answer = self.multiply(answer, value)
            value = self.multiply(value, value)
            exponent >>= 1
        return answer

    def expression(self, text):
        """Exact field-polynomial interpretation; no eval or CAS is used."""
        node = ast.parse(text.replace('^', '**').replace('lambda', 'lam'), mode='eval')

        def visit(value):
            if isinstance(value, ast.Constant):
                assert type(value.value) is int
                return {} if value.value == 0 else {0: (Q(value.value), Q(0))}
            if isinstance(value, ast.Name):
                assert value.id in ('k', 'lam')
                return {0: (Q(0), Q(1))} if value.id == 'k' else {1: ONE}
            if isinstance(value, ast.UnaryOp):
                assert isinstance(value.op, (ast.USub, ast.UAdd))
                return self.scale(visit(value.operand), Q(-1 if isinstance(value.op, ast.USub) else 1))
            assert isinstance(value, ast.BinOp)
            if isinstance(value.op, ast.Pow):
                assert isinstance(value.right, ast.Constant) and type(value.right.value) is int
                return self.power(visit(value.left), value.right.value)
            a, b = visit(value.left), visit(value.right)
            if isinstance(value.op, ast.Add):
                return self.add(a, b)
            if isinstance(value.op, ast.Sub):
                return self.add(a, self.scale(b, Q(-1)))
            if isinstance(value.op, ast.Mult):
                return self.multiply(a, b)
            assert isinstance(value.op, ast.Div) and set(b) == {0}
            return self.multiply(a, {0: self.finverse(b[0])})

        return visit(node.body)

    def source(self):
        data = json.loads((HERE/SOURCE_INPUTS[3]).read_text())
        seed = [self.expression(value) for value in data['seed']]
        assert all(set(value).issubset({0}) for value in seed)
        kernel = list(map(Q, data['kernel']))
        alpha = [self.add(value, {} if slope == 0 else {1: (slope, Q(0))})
                 for value, slope in zip(seed, kernel)]
        family = data['family']
        expected = {
            'a1': '(k**2+3)/(2-2*k**2)',
            'a2': '-(k**2+2*k+3)/(2*(k+1)**2)',
            'b1': '(k-3)*(k**2+2*k+3)/((k-1)**2*(k+1))',
            'b2': '-2*(k**2+1)*(k**2-2*k-1)*(k**2+2*k+3)/((k-1)**3*(k+1)**3)'
        }
        for key, value in expected.items():
            assert self.expression(family[key]) == self.expression(value)
        p = [{0: ONE}, self.expression(family['a1']), self.expression(family['a2'])]
        r = [{0: ONE}, self.expression(family['b1']), self.expression(family['b2'])]
        return data, alpha, kernel, p, r

    @staticmethod
    def encode(poly):
        return [[degree, str(value[0]), str(value[1])] for degree, value in sorted(poly.items())]

    @staticmethod
    def decode(terms):
        result = {}
        for degree, a, b in terms:
            assert degree >= 0 and degree not in result
            value = (Q(a), Q(b))
            if value != ZERO:
                result[degree] = value
        return result

    @staticmethod
    def tensor():
        tensor = [[Q(0)]*542 for _ in range(74)]
        lines = (HERE/SOURCE_INPUTS[0]).read_text().splitlines()
        assert lines[0] == '30 18 74 542'
        for line in lines[1:]:
            row, col, value = line.split()
            tensor[int(row)][int(col)] += Q(value)
        assert [row[540] for row in tensor] == [Q(i == 72) for i in range(74)]
        assert [row[541] for row in tensor] == [Q(i == 73) for i in range(74)]
        return tensor

    def generate(self):
        data, alpha, kernel, p, r = self.source()
        tensor = self.tensor()

        def entry(row, col):
            value = {}
            for i in range(30):
                value = self.add(value, self.scale(alpha[i], tensor[row][18*i+col]))
            pieces = []
            for degree, (a, b) in sorted(value.items()):
                coefficient = '('+str(a)+'+('+str(b)+')*k)'
                pieces.append('sub('+coefficient+',R)' + ('*lambda^'+str(degree) if degree else ''))
            return '+'.join(pieces) if pieces else '0_R'

        script = [
            '-- Complete actual family2 fibre at '+self.info['modulus']+'.',
            'P=QQ[k]; K0=toField(P/ideal('+self.info['modulus']+')); R=K0[lambda];',
            'L=matrix{'+','.join('{'+','.join(entry(row, col) for col in range(18))+'}'
                               for row in range(74))+'};',
            'U=matrix{'+','.join('{'+str(int(row == 72))+'}' for row in range(74))+'};',
            'print("actual matrix ready at '+self.case+'");',
            'V=gens kernel transpose L; E=transpose U*V; J=ideal E;',
            'print("full polynomial left kernel computed");',
            'ff=openOut "research/computations/'+self.stem+'-evaluations.txt";',
            'ff << gens gb J << endl; close ff;',
            'print("full target evaluation ideal saved");',
            'if J==ideal(1_R) then (',
            ' c=matrix{{1_R}} // E; n=V*c;',
            ' assert(transpose n*L==0); assert(transpose n*U==matrix{{1_R}});',
            ' ff=openOut "research/computations/'+self.stem+'-dual.txt";',
            ' for row from 0 to 73 do ff << row << " " << toString n_(row,0) << endl;',
            ' close ff; print("complete polynomial dual saved")',
            ');', 'exit 0;'
        ]
        (HERE/(self.stem+'.m2')).write_text('\n'.join(script)+'\n')
        print('Generated actual complete fibre over QQ[k]/('+self.info['modulus']+')[lambda].')
        print('Every rational source denominator was inverted as a field unit.')

    def regenerate(self):
        data, alpha, kernel, p, r = self.source()
        dual = []
        for row, line in enumerate((HERE/(self.stem+'-dual.txt')).read_text().splitlines()):
            index, value = line.split(maxsplit=1)
            assert int(index) == row
            dual.append(self.expression(value))
        inputs = SOURCE_INPUTS+[self.stem+'.m2', self.stem+'-dual.txt',
                               self.stem+'-evaluations.txt']
        self.cert.write_text(json.dumps({
            'coordinate_sha256': {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                                  for name in inputs},
            'case': self.case, 'defining_polynomial': self.info['modulus'],
            'discriminant': self.info['discriminant'],
            'alpha': list(map(self.encode, alpha)), 'dual': list(map(self.encode, dual)),
            'direction_p': list(map(self.encode, p)), 'direction_r': list(map(self.encode, r)),
            'scope': 'Second rational endpoint family; both quadratic roots; every lambda',
            'status': 'EXACT FIELD POLYNOMIAL CERTIFICATE VERIFIED BY THIS SCRIPT'
        }, indent=2)+'\n')

    def verify(self):
        info = json.loads(self.cert.read_text())
        assert info['case'] == self.case and info['defining_polynomial'] == self.info['modulus']
        discriminant = int(self.info['discriminant'])
        assert info['discriminant'] == discriminant != 0
        assert discriminant < 0 or math.isqrt(discriminant)**2 != discriminant
        assert self.relation[1]**2+4*self.relation[0] == discriminant
        for name, expected in info['coordinate_sha256'].items():
            assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected, name
        source, actual_alpha, kernel, actual_p, actual_r = self.source()
        alpha = list(map(self.decode, info['alpha']))
        dual = list(map(self.decode, info['dual']))
        p, r = [list(map(self.decode, info[key])) for key in ('direction_p', 'direction_r')]
        assert alpha == actual_alpha and p == actual_p and r == actual_r
        assert len(alpha) == 30 and len(dual) == 74 and dual[72] == {0: ONE}
        matrix = [[Q(value) for value in row] for row in
                  json.loads((HERE/SOURCE_INPUTS[2]).read_text())['matrix']]
        assert len(matrix) == 32 and all(len(row) == 30 for row in matrix)
        echelon = [row[:] for row in matrix]
        rank = 0
        for col in range(30):
            pivot = next((i for i in range(rank, len(echelon)) if echelon[i][col]), None)
            if pivot is None:
                continue
            echelon[rank], echelon[pivot] = echelon[pivot], echelon[rank]
            coefficient = echelon[rank][col]
            echelon[rank] = [v/coefficient for v in echelon[rank]]
            for i in range(rank+1, len(echelon)):
                coefficient = echelon[i][col]
                if coefficient:
                    echelon[i] = [v-coefficient*w for v, w in zip(echelon[i], echelon[rank])]
            rank += 1
        assert rank == 29 and len(kernel) == 30 and any(kernel)

        def tmultiply(first, second):
            answer = [{} for _ in range(len(first)+len(second)-1)]
            for i, a in enumerate(first):
                for j, b in enumerate(second):
                    answer[i+j] = self.add(answer[i+j], self.multiply(a, b))
            return answer

        def tpower(value, exponent):
            answer = [{0: ONE}]
            for _ in range(exponent):
                answer = tmultiply(answer, value)
            return answer

        top = []
        for i in range(4):
            top.extend([{}]+tmultiply(tpower(p, i), tpower(r, 3-i)))
        assert len(top) == 32
        for row, expected in zip(matrix, top):
            value = {}
            for coefficient, element in zip(row, alpha):
                value = self.add(value, self.scale(element, coefficient))
            assert value == expected
        for coordinate, slope in zip(alpha, kernel):
            assert set(coordinate).issubset({0, 1})
            assert coordinate.get(1, ZERO) == (slope, Q(0))
        resultant = {}
        sylvester = [[p[2], p[1], p[0], {}], [{}, p[2], p[1], p[0]],
                     [r[2], r[1], r[0], {}], [{}, r[2], r[1], r[0]]]
        for permutation in itertools.permutations(range(4)):
            sign = (-1)**sum(permutation[i] > permutation[j] for i in range(4) for j in range(i+1, 4))
            term = {0: ONE}
            for row, col in enumerate(permutation):
                term = self.multiply(term, sylvester[row][col])
            resultant = self.add(resultant, self.scale(term, Q(sign)))
        assert resultant == self.expression(source['family']['resultant']) and set(resultant) == {0}
        assert resultant[0] != ZERO
        tensor = self.tensor()
        for col in range(18):
            value = {}
            for row in range(74):
                entry = {}
                for i in range(30):
                    entry = self.add(entry, self.scale(alpha[i], tensor[row][18*i+col]))
                value = self.add(value, self.multiply(dual[row], entry))
            assert not value, ('actual tensor column', col, value)
        print('PASS '+self.case+': irreducible quadratic, all source direction/seed/slope coefficients rederived.')
        print('PASS '+self.case+': rank29 actual top, complete affine fibre, primitive homogeneous resultant.')
        print('PASS '+self.case+': all 18 polynomial tensor identities and n^T u=1.')
        print('PROVED '+self.case+': both geometric roots excluded, for every lambda.')


if __name__ == '__main__':
    selected = [arg for arg in sys.argv[1:] if arg in CASES] or list(CASES)
    for case in selected:
        audit = Audit(case)
        if '--generate' in sys.argv:
            audit.generate()
        else:
            if '--regenerate' in sys.argv:
                audit.regenerate()
            audit.verify()
