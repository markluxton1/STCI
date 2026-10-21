#!/usr/bin/env python3
"""Structured exact global-sextic cubic obstruction in the (2,12) lane.

Reads the previous proposed exact symbol matrices and accepted K1 model as
inputs, writes a chart-free matrix/model, and certifies one nonzero 48-minor.
Uses rational sparse coefficient polynomials and standard-library Python only.
No Groebner basis or global emptiness assertion is made by this exporter.
"""

from fractions import Fraction as Q
from pathlib import Path
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
base_file = HERE/'conditional_2_12_symbol_map_2026_10_20.py'
spec = importlib.util.spec_from_file_location('symbol_map_helpers',base_file)
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)

NAMES = [f'{c}{j}' for c in 'abc' for j in range(3)]+[f'h{j}' for j in range(12)]


def const(x):
    return {():Q(x)} if x else {}


def var(i):
    return {(i,):Q(1)}


def add(*ps):
    out = {}
    for p in ps:
        for m,c in p.items():
            out[m] = out.get(m,Q(0))+c
    return {m:c for m,c in out.items() if c}


def scale(p,c):
    return {m:c*x for m,x in p.items() if c*x}


def mul(p,q):
    out = {}
    for m,c in p.items():
        for n,d in q.items():
            mn = tuple(sorted(m+n))
            out[mn] = out.get(mn,Q(0))+c*d
    return {m:c for m,c in out.items() if c}


def fmt(p):
    terms = []
    for m,c in sorted(p.items(),key=lambda x:(len(x[0]),x[0])):
        factors = '*'.join(NAMES[i] for i in m)
        coefficient = '' if abs(c)==1 and factors else str(abs(c))
        terms.append(('-' if c<0 else '+')+coefficient+
                     ('*' if coefficient and factors else '')+factors)
    out = ''.join(terms)
    return out[1:] if out.startswith('+') else (out or '0')


def evaluate(p,point):
    out = Q(0)
    for m,c in p.items():
        for i in m:
            c *= point[i]
        out += c
    return out


def text_mat(a):
    return [[fmt(p) for p in row] for row in a]


def conv(a,b):
    out = [{} for _ in range(len(a)+len(b)-1)]
    for i,p in enumerate(a):
        for j,q in enumerate(b):
            out[i+j] = add(out[i+j],mul(p,q))
    return out


def main():
    symbol_path = HERE/'conditional_2_12_symbol_map_2026_10_20.json'
    accepted_path = HERE/'generalization_quadratic_root_curve_universal_incidence.json'
    symbol = json.loads(symbol_path.read_text())
    accepted = json.loads(accepted_path.read_text())
    M = [[Q(x) for x in row] for row in symbol['symbol_matrix_33_by_23']]
    C = [[Q(x) for x in row] for row in symbol['cubic_layer_matrix_40_by_23']]
    f = [[var(3*i+j) for j in range(3)] for i in range(3)]
    # h0,...,h5 multiply z^-6,...,z^-1 times u; h6,...,h11 times v.
    hu2,hu1,hv2,hv1 = (var(9+i) for i in (4,5,10,11))
    a,b,c = f
    # Accepted G0=nonnegative_z(Df-fh). Only these four h coordinates enter.
    G0 = [
        [scale(add(mul(a[1],hu1),mul(a[2],hu2)),-1),scale(mul(a[2],hu1),-1)],
        [scale(add(mul(b[1],hu1),mul(b[2],hu2),mul(a[1],hv1),mul(a[2],hv2)),-1),
         scale(add(mul(b[2],hu1),mul(a[2],hv1)),-1)],
        [scale(add(scale(a[2],Q(3,4)),mul(c[1],hu1),mul(c[2],hu2),mul(b[1],hv1),mul(b[2],hv2)),-1),
         scale(add(mul(c[2],hu1),mul(b[2],hv1)),-1)],
        [scale(add(scale(b[2],Q(3,8)),mul(c[1],hv1),mul(c[2],hv2)),-1),
         scale(mul(c[2],hv1),-1)],
    ]
    block = []
    # Unknown vector is (actual global sextic c23, alpha9, ell8, m8).
    for i in range(33):
        comp,z = divmod(i,11)
        alpha = [scale(f[comp][z-j],-1) if 0<=z-j<=2 else {} for j in range(9)]
        block.append([const(x) for x in M[i]]+alpha+[{} for _ in range(16)])
    for i in range(40):
        comp,z = divmod(i,10)
        alpha = [scale(G0[comp][z-j],-1) if 0<=z-j<=1 else {} for j in range(9)]
        ell = []
        for normal in range(2):
            for j in range(8):
                fcomp = comp-normal
                ell.append(scale(f[fcomp][z-j],-1)
                           if 0<=fcomp<=2 and 0<=z-j<=2 else {})
        block.append([const(x) for x in C[i]]+alpha+ell)
    assert len(block)==73 and all(len(row)==48 for row in block)

    # Quadric-line reduction. Canonical norm alpha has a quadratic expression
    # in g's five coefficients, avoiding all resultant or alpha variables.
    g = [c[0],add(c[1],scale(b[0],Q(-1,2))),
         add(c[2],scale(b[1],Q(-1,2)),scale(a[0],Q(1,4))),
         add(scale(a[1],Q(1,4)),scale(b[2],Q(-1,2))),scale(a[2],Q(1,4))]
    Ag = [g[0],{},{},g[3],{}]
    Bg = [{},g[1],{},{},g[4]]
    Cg = [{},{},g[2],{},{}]
    norm_alpha = [add(x,y,z,scale(xy,-1),scale(xz,-1),scale(yz,-1))
                  for x,y,z,xy,xz,yz in zip(conv(Ag,Ag),conv(Bg,Bg),conv(Cg,Cg),
                                           conv(Ag,Bg),conv(Ag,Cg),conv(Bg,Cg))]
    norm_R = conv(norm_alpha,g)
    assert all(not p for i,p in enumerate(norm_R) if i%3)
    ap,bp = conv(norm_alpha,a),conv(norm_alpha,b)
    norm_symbol = [add(ap[3*j-2],scale(bp[3*j-1],-1),scale(norm_R[3*j],-j))
                   for j in range(1,4)]
    # Verify exactly that only three of the original eleven remain.
    target = [conv(norm_alpha,p) for p in f]
    direct_L = [add(*(scale(target[comp][j],Q(row[11*comp+j]))
                     for comp in range(3) for j in range(11)))
                for row in symbol['annihilator_11_by_33']]
    assert all(not direct_L[i] for i in (0,1,2,4,5,7,8,10))
    assert direct_L[3] == scale(norm_symbol[0],4)
    assert direct_L[6] == scale(norm_symbol[1],2)
    assert direct_L[9] == scale(norm_symbol[2],4)
    G = [{} for _ in range(5)]
    for comp in range(4):
        for j,p in enumerate(G0[comp]):
            degree = 3-comp+j
            G[degree] = add(G[degree],scale(p,Q(-1,2)**(3-comp)))
    qline_D = [scale(g[i+1],i+1) if i<4 else {} for i in range(7)]
    for j,p in enumerate(G):
        qline_D[j+2] = add(qline_D[j+2],scale(p,-3))
    # g4^3*remainder(D,g), valid equivalently to remainder=0 on g4 !=0.
    prem = list(qline_D)
    for degree in range(6,3,-1):
        leading = prem[degree]
        prem = [mul(p,g[4]) for p in prem]
        for j,p in enumerate(g):
            prem[degree-4+j] = add(prem[degree-4+j],scale(mul(leading,p),-1))
        assert not prem[degree]
    qline_pseudorem = prem[:4]

    # Intrinsic 16-by-5 quotient: H0(O(1,1))*f and q^3 inside H0(O(3,3)).
    quotient = []
    q3 = {(0,0):Q(1),(1,1):Q(3,2),(2,2):Q(3,4),(3,3):Q(1,8)}
    for comp in range(4):
        for z in range(4):
            row = []
            for normal in range(2):
                for j in range(2):
                    fcomp=comp-normal
                    row.append(f[fcomp][z-j]
                               if 0<=fcomp<=2 and 0<=z-j<=2 else {})
            quotient.append(row+[const(q3.get((comp,z),Q(0)))])

    seed = [Q(4),Q(0),Q(1),Q(0),Q(0),Q(0),Q(-8),Q(0),Q(1)]+[
        Q(x) for x in accepted['smooth_example']['h_solution']]
    numeric = [[evaluate(p,seed) for p in row] for row in block]
    rank = len(helpers.rref(numeric)[1])
    assert rank == 48
    rows = helpers.rref(helpers.transpose(numeric))[1]
    minor_determinant = helpers.determinant([numeric[i] for i in rows])
    assert minor_determinant
    rank39 = len(helpers.rref([[row[j] for j in list(range(23))+list(range(32,48))]
                            for row in numeric])[1])
    assert rank39 == 39
    qnumeric = [[evaluate(p,seed) for p in row] for row in quotient]
    assert len(helpers.rref(qnumeric)[1]) == 5

    # Polynomial K1 equations are reconstructed from the accepted saved model.
    first = []
    for row,rhs in zip(accepted['A_f'],accepted['d_f']):
        terms = [f'({entry})*h{j}' for j,entry in enumerate(row) if entry!='0']
        first.append('+'.join(terms)+f'-({rhs})')
    matrix_text = text_mat(block)
    quotient_text = text_mat(quotient)
    model_path = Path(__file__).with_suffix('.m2')
    unknowns = [f'cc{i}' for i in range(23)]+[f'al{i}' for i in range(9)]+[
        f'el{i}' for i in range(8)]+[f'mm{i}' for i in range(8)]
    lines = [
        '-- Exact structured global-sextic cubic model. No elimination is run.',
        'R=QQ['+','.join(NAMES+unknowns)+',MonomialOrder=>GRevLex];',
        'firstEquations={'+','.join(first)+'};',
        'globalCubicMatrix=matrix{'+','.join('{'+','.join(row)+'}' for row in matrix_text)+'};',
        'cubicQuotientMatrix=matrix{'+','.join('{'+','.join(row)+'}' for row in quotient_text)+'};',
        'unknownVector=transpose matrix{{'+','.join(unknowns)+'}};',
        'globalCubicEquations=flatten entries(globalCubicMatrix*unknownVector);',
        'globalCubicIncidence=ideal join(firstEquations,globalCubicEquations);',
        'witnessRows={'+','.join(map(str,rows))+'};',
        'globalCubicWitnessMatrix=submatrix(globalCubicMatrix,witnessRows,toList(0..47));',
        '-- Its determinant defines the scalar witness; not expanded on load.',
        'gCoefficients={'+','.join(fmt(p) for p in g)+'};',
        'normAlpha={'+','.join(fmt(p) for p in norm_alpha)+'};',
        'normSymbolEquations={'+','.join(fmt(p) for p in norm_symbol)+'};',
        'qlinePseudoRemainders={'+','.join(fmt(p) for p in qline_pseudorem)+'};',
        '-- These four remainders are necessary on g4!=0 and gcd(alpha,g)=1.',
        '-- Together with norm alpha, this includes the simple distinct-cube-root open.',
        'qlineNecessaryIdeal=ideal join(firstEquations,normSymbolEquations,qlinePseudoRemainders);',
        '-- On the g0*g4!=0 torus/projective chart one may normalize g0=g4=1:',
        'qlineNormalizedIdeal=qlineNecessaryIdeal+ideal(gCoefficients#0-1,gCoefficients#4-1);',
        '-- Necessity requires alpha=(al0,...,al8) nonzero, root bpf/reduced;',
        '-- retain those opens by projective charts or genuine saturation.',
        '-- This exporter DOES NOT compute minors(48,globalCubicMatrix).',
        'print "MODEL_READY: K1 plus exact global cubic incidence; no elimination run";',
    ]
    model_path.write_text('\n'.join(lines)+'\n')
    out = {
        'status':'new structured exact reduction; independent review pending',
        'inputs':[{ 'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in (symbol_path,accepted_path)],
        'field':'characteristic zero',
        'coefficient_variables':NAMES,
        'unknown_vector':unknowns,
        'G0_coefficients_ascending_z':text_mat(G0),
        'matrix_73_by_48':matrix_text,
        'unknown_interpretation':'c23 actual global k sextic coefficients, alpha9, ell8, m8',
        'rank_criterion':'On reduced basepoint-free roots satisfying K1, nonzero global sextic cubic lift iff rank(matrix)<48.',
        'why_nonzero_alpha':'The c23+ell16 submatrix has rank39 for every reduced root: a zero-alpha kernel would require f dividing q^3, impossible for reduced bidegree(2,2) f.',
        'quotient_matrix_16_by_5':quotient_text,
        'quotient_interpretation':'H0(O(3,3))/(f*H0(O(1,1))+k*q^3), rank11 for every reduced root',
        'cohomology_dimensions':{'H0_O33':16,'f_H0_O11':4,'H0_OZ33':12,'q3_class':1,'obstruction_quotient':11},
        'necessary_scalar_obstruction':{
            'definition':'determinant of indicated 48-row submatrix of matrix_73_by_48',
            'rows_zero_based':rows,
            'seed_determinant':str(minor_determinant),
            'seed_full_rank':rank,
            'seed_c_plus_ell_rank':rank39,
            'interpretation':'Nonzero on the accepted first-compatible torsion-two seed; therefore a genuine nonautomatic obstruction on its K1 component. Its vanishing is necessary, not sufficient.'},
        'quadric_restriction':{
            'q_symbol':'l=u+(z/2)*v',
            'g':'c-(z/2)*b+(z^2/4)*a',
            'first_identity':'alpha*g=R(z^3), deg R<=4',
            'cubic_necessary':'Rprime(z^3)-alpha*G0(z,-z/2,1) is divisible by g',
            'denominator_free':'g divides alpha*(gprime-3*z^2*G0(z,-z/2,1)); retain alpha zeros and z=0,infinity',
            'g_coefficients_ascending':[fmt(p) for p in g],
            'G_coefficients_ascending':[fmt(p) for p in G],
            'norm_alpha_coefficients_ascending':[fmt(p) for p in norm_alpha],
            'norm_alpha_identity':'g(omega*z)*g(omega^2*z)=A^2+B^2+C^2-A*B-A*C-B*C, A=g0+g3*z^3,B=g1*z+g4*z^4,C=g2*z^2',
            'remaining_three_symbol_equations':[fmt(p) for p in norm_symbol],
            'eight_other_symbol_equations_identically_zero':True,
            'qline_four_pseudoremainders':[fmt(p) for p in qline_pseudorem],
            'pseudoremainder_scaling':'g4^3*rem(gprime-3*z^2*G,g)',
            'small_model':'K1 sixteen equations + three norm-symbol cubics +four qline pseudoremainders, no alpha variables',
            'small_model_open':'g4!=0 and gcd(alpha,g)=1; simple distinct-cube root open suffices',
            'normalization':'On g0*g4!=0 use projective root scaling and C0 torus weights(z,u,v)=(1,4,3) to set g0=g4=1'},
        'model_file':str(model_path),
        'limitations':['Universal rank<48 locus not computed empty.',
                       'Picard torsion12 and complete K2 intersection not eliminated.',
                       'No global pair, degree12 standard-basis certificate, or Bezout certificate.'],
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'model':str(model_path),'rank':rank,'minor_rows':rows,
                      'seed_minor_determinant':str(minor_determinant),
                      'rank11_quotient':True}))


if __name__ == '__main__':
    main()
