#!/usr/bin/env python3
"""Clear/verify the generic first rational endpoint family's polynomial dual.

Default verification uses exact standard-library arithmetic only.
--regenerate uses SymPy to clear the saved M2 rational dual and ancestor.
The dual proves exclusion only where its displayed denominator is nonzero.
"""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import sys

HERE=Path(__file__).resolve().parent
INDEX=next((int(value) for value in sys.argv[1:] if value.isdecimal()),1)
assert INDEX in (1,2,3,4)
STEM='session-localcoh-origin-family-'+str(INDEX)
CERT=HERE/(STEM+'-polynomial-dual.json')

def regenerate():
    import sympy as s
    k,lam=s.symbols('k lam')
    dual=[]
    for row,line in enumerate((HERE/(STEM+'-generic-dual.txt')).read_text().splitlines()):
        index,value=line.split(maxsplit=1)
        assert int(index)==row
        dual.append(s.cancel(s.sympify(value.replace('^','**').replace('lambda','lam'),
                                      locals={'k':k,'lam':lam})))
    denominator=s.Integer(1)
    for value in dual:
        for coefficient in s.Poly(value,lam).all_coeffs():
            denominator=s.lcm(denominator,s.denom(s.cancel(coefficient)))
    saved=json.loads((HERE/(STEM+'-seed.json')).read_text())
    seed=[s.sympify(value,locals={'k':k}) for value in saved['seed']]
    kernel=[s.Rational(value) for value in saved['kernel']]
    ancestor_denominator=s.Integer(1)
    for value in seed:
        ancestor_denominator=s.lcm(ancestor_denominator,s.denom(s.cancel(value)))
    alpha=[s.cancel(ancestor_denominator*value)+lam*ancestor_denominator*correction
           for value,correction in zip(seed,kernel)]
    polynomial_dual=[s.cancel(denominator*value) for value in dual]
    def terms(value):
        return [[i,j,str(coefficient)] for (i,j),coefficient
                in s.Poly(value,k,lam).terms() if coefficient]
    inputs=['localcoh-incidence-tensor.txt','localcoh-incidence-bases.txt',
            'localcoh-symbol-top.json',STEM+'-seed.json',STEM+'-generic-dual.txt']
    CERT.write_text(json.dumps({
        'coordinate_sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in inputs},
        'alpha':[terms(value) for value in alpha],
        'dual':[terms(value) for value in polynomial_dual],
        'ancestor_denominator':terms(ancestor_denominator),
        'dual_on_u':terms(denominator),
        'denominator_factorization':str(s.factor(denominator)),
        'scope':'origin family '+str(INDEX)+'; k outside all displayed denominator roots; every lambda',
        'status':'POLYNOMIAL IDENTITY TO BE VERIFIED'
    },indent=2)+'\n')
    print('Cleared ancestor denominator:',s.factor(ancestor_denominator))
    print('Cleared dual denominator:',s.factor(denominator))

def decode(terms):
    result={}
    for i,j,value in terms:
        assert i>=0 and j>=0 and (i,j) not in result
        if Q(value): result[i,j]=Q(value)
    return result

def add(first,second):
    result=dict(first)
    for power,value in second.items():
        result[power]=result.get(power,Q(0))+value
        if not result[power]:del result[power]
    return result

def scale(poly,value):
    return {power:coefficient*value for power,coefficient in poly.items() if coefficient*value}

def multiply(first,second):
    result={}
    for (i,j),a in first.items():
        for (l,m),b in second.items():
            power=(i+l,j+m)
            result[power]=result.get(power,Q(0))+a*b
            if not result[power]:del result[power]
    return result

def verify():
    data=json.loads(CERT.read_text())
    for name,expected in data['coordinate_sha256'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected,name
    alpha=list(map(decode,data['alpha']))
    dual=list(map(decode,data['dual']))
    target=decode(data['dual_on_u'])
    assert len(alpha)==30 and len(dual)==74 and target
    assert dual[72]==target
    products=[[{} for col in range(18)] for i in range(30)]
    lines=(HERE/'localcoh-incidence-tensor.txt').read_text().splitlines()
    assert lines[0]=='30 18 74 542'
    for line in lines[1:]:
        row,col,value=line.split();row,col=int(row),int(col)
        if col<540:
            i,j=divmod(col,18)
            products[i][j]=add(products[i][j],scale(dual[row],Q(value)))
    for col in range(18):
        total={}
        for i in range(30):total=add(total,multiply(products[i][col],alpha[i]))
        assert not total,('tensor identity',col,len(total))
    print('PASS: all 18 cleared polynomial tensor identities over QQ[k,lambda].')
    print('PASS: n^T u is exactly the displayed nonzero denominator polynomial.')
    print('PROVED: origin family',INDEX,'excludes u away from that polynomial\'s roots, for every lambda.')
    print('OPEN: primitive exceptional denominator roots and any uncertified origin families.')

if __name__=='__main__':
    if '--regenerate' in sys.argv:regenerate()
    verify()
