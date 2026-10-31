#!/usr/bin/env python3
"""Check the saved degree-fifteen dual in the complete actual tensor.

The certificate contains the exact dual. This checker reconstructs the matrix
from its mathematical inputs and checks every polynomial identity; construction
inverses, run records and earlier search attempts are unnecessary.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
STEM = 'general-localcoh-family2-degree15-corank-one-2026-10-14-attempt06'
ARITHMETIC = 'evening_localcoh_family2_exception_fields_2026_10_13.py'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verify', action='store_true', help='Retained command compatibility; checking is always performed.')
    parser.add_argument('--stem', default=STEM, choices=[STEM], help='Saved complete degree-fifteen certificate.')
    args = parser.parse_args()
    record = json.loads((HERE / (args.stem + '-certificate.json')).read_text())
    spec = importlib.util.spec_from_file_location('accepted_arithmetic', HERE / ARITHMETIC)
    arithmetic = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(arithmetic)
    assert set(record['sha256']) == set(arithmetic.INPUTS + [ARITHMETIC]), 'mathematical input closure'
    for name, digest in record['sha256'].items():
        assert hashlib.sha256((HERE / name).read_bytes()).hexdigest() == digest, name
    audit = arithmetic.Audit('degree15')
    assert record['modulus_coefficients'] == list(map(str, audit.mod))
    dual = list(map(audit.decode, record['dual']))
    assert len(dual) == 74
    assert dual[72] == {0: audit.one}
    assert all(all(degree <= 2 for degree in polynomial) for polynomial in dual)
    source, alpha, kernel, p, r = audit.source()
    matrix = audit.matrix(alpha)
    for column in range(18):
        total = {}
        for row in range(74):
            total = audit.add(total, audit.mul(dual[row], matrix[row][column]))
        assert not total, ('polynomial dual failure', column)
    print('PASS: normalized degree<=2 dual; all18 actual-tensor column identities modulo full degree15 polynomial; every affine lambda.')
    print('Inherited tensor/top-map interpretations remain the stated mathematical premises.')


if __name__ == '__main__':
    main()
