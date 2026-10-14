#!/usr/bin/env python3
"""Verify only the NEW degree15 corank-one dual, in the accepted actual tensor.

This does not rerun the accepted tensor/top-basis/rank29 verifiers. It checks
new polynomial dual identities modulo the full degree15 polynomial, rather
than numerical roots or rank samples. An existing certificate can be checked
with --verify; without that option, the exact M2 output is parsed and bound.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import re

HERE=Path(__file__).resolve().parent
STEM='general-localcoh-family2-degree15-corank-one-2026-10-14-attempt02'
spec=importlib.util.spec_from_file_location('accepted_arithmetic',HERE/'evening_localcoh_family2_exception_fields_2026_10_13.py')
arithmetic=importlib.util.module_from_spec(spec)
spec.loader.exec_module(arithmetic)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify',action='store_true')
    args=parser.parse_args()
    audit=arithmetic.Audit('degree15')
    certificate=HERE/(STEM+'-certificate.json')
    if args.verify:
        record=json.loads(certificate.read_text())
        for name,digest in record['sha256'].items():
            assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==digest,name
        assert record['modulus_coefficients']==list(map(str,audit.mod))
        dual=list(map(audit.decode,record['dual']))
    else:
        dual=[]
        for row,line in enumerate((HERE/(STEM+'-dual.txt')).read_text().splitlines()):
            index,expression=line.split(maxsplit=1)
            assert int(index)==row
            expression=re.sub(r'\bz\b','k',expression)
            dual.append(audit.expr(expression))
        names=arithmetic.INPUTS+[STEM+'.m2',STEM+'-dual.txt',Path(__file__).name]
        record={
            'case':'degree15',
            'modulus_coefficients':list(map(str,audit.mod)),
            'sha256':{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in names},
            'dual':list(map(audit.encode,dual)),
            'scope':'Accepted actual quartic-ancestor tensor; second rational endpoint family; every root of degree15 factor; every affine lower lift lambda.',
            'inherited_scope':'Accepted actual tensor and coordinate/top-map interpretations are used without re-verification.',
            'new_checks':'Polynomial normalized dual degree at most2; all18 tensor-column identities modulo entire degree15 polynomial; target coordinate72 equals1.',
        }
    assert len(dual)==74
    assert dual[72]=={0:audit.one}
    assert all(all(degree<=2 for degree in polynomial) for polynomial in dual)
    source,alpha,kernel,p,r=audit.source()
    L=audit.matrix(alpha)
    for column in range(18):
        total={}
        for row in range(74):
            total=audit.add(total,audit.mul(dual[row],L[row][column]))
        assert not total,('new polynomial dual failure',column)
    if not args.verify:
        certificate.write_text(json.dumps(record,indent=2)+'\n')
    print('PASS NEW CERTIFICATE: normalized degree<=2 dual; all18 actual-tensor column identities modulo full degree15 polynomial; every affine lambda.',flush=True)
    print('Inherited tensor/top-map interpretations accepted; no inherited verifier rerun.',flush=True)

if __name__=='__main__':
    main()
