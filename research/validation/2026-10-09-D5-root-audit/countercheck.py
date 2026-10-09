#!/usr/bin/env python3
"""Independent signed-partition enumeration, without reflection closure/HNF.

This checks the finite lattice scope of the written signed-component proof.
It does not classify surfaces or give an STCI pair. Its enumeration is
different from the owner's reflection-closure search and integer HNF check.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json


def partitions(items):
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield ((first,),) + p
        for j, block in enumerate(p):
            yield p[:j] + ((first,) + block,) + p[j+1:]


ROOTS = tuple(tuple(a if n == i else b if n == j else 0 for n in range(5))
              for i, j in combinations(range(5), 2)
              for a, b in product((-1, 1), repeat=2))


def configurations(block):
    if len(block) == 1:
        yield (block, 'unused', ())
        return
    yield (block, 'D', ())
    for signs in product((-1, 1), repeat=len(block)-1):
        yield (block, 'A', (1,) + signs)


def supported(root, block):
    return all(value == 0 for i, value in enumerate(root) if i not in block)


def span_contains(root, configuration):
    for block, kind, signs in configuration:
        if kind == 'unused' and root[block[0]]:
            return False
        if kind == 'A' and sum(s * root[i] for s, i in zip(signs, block)):
            return False
    return True


def lattice_contains(root, configuration):
    return span_contains(root, configuration) and all(
        sum(root[i] for i in block) % 2 == 0
        for block, kind, signs in configuration if kind == 'D')


def root_set(configuration):
    found = set()
    for block, kind, signs in configuration:
        if kind == 'unused':
            continue
        for root in ROOTS:
            if supported(root, block) and (kind == 'D' or
                    sum(s * root[i] for s, i in zip(signs, block)) == 0):
                found.add(root)
    return frozenset(found)


def type_name(configuration):
    parts = []
    for block, kind, signs in configuration:
        if kind == 'unused':
            continue
        if kind == 'A':
            parts.append('A' + str(len(block)-1))
        elif len(block) == 2:
            parts.extend(('A1', 'A1'))
        elif len(block) == 3:
            parts.append('A3')
        else:
            parts.append('D' + str(len(block)))
    return '+'.join((str(n) if n > 1 else '') + name
                    for name, n in sorted(Counter(parts).items())) or 'empty'


def main():
    seen = {}
    counts = Counter()
    exceptions = Counter()
    assert len(ROOTS) == 40 and len(set(ROOTS)) == 40
    all_partitions = list(partitions(list(range(5))))
    assert len(all_partitions) == 52
    for partition in all_partitions:
        for configuration in product(*(tuple(configurations(b)) for b in partition)):
            roots = root_set(configuration)
            assert roots not in seen, 'Signed block enumeration should be unique'
            seen[roots] = configuration
            typename = type_name(configuration)
            counts[typename] += 1
            span_roots = {r for r in ROOTS if span_contains(r, configuration)}
            lattice_roots = {r for r in ROOTS if lattice_contains(r, configuration)}
            assert lattice_roots == set(roots)
            missing = span_roots - lattice_roots
            dblocks = [b for b, k, s in configuration if k == 'D']
            predicted = {r for r in ROOTS if any(
                sum(bool(r[i]) for i in b1) == 1 and
                sum(bool(r[i]) for i in b2) == 1
                for b1, b2 in combinations(dblocks, 2))}
            assert missing == predicted
            if missing:
                assert typename in ('4A1', '2A1+A3')
                assert len(dblocks) == 2
                assert len(missing) == (16 if typename == '4A1' else 24)
                exceptions[typename] += 1
    assert len(seen) == 428
    assert exceptions == {'4A1': 15, '2A1+A3': 10}
    source = Path(__file__).resolve()
    report = {'status': 'PASS', 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'method': '52 set partitions and all balanced sign choices or full D blocks; no reflection closure or HNF',
              'embedded_root_subsystems': len(seen), 'type_counts': dict(sorted(counts.items())),
              'nonprimitive_embeddings': dict(exceptions),
              'scope': 'Finite D5 lattice check supporting the signed-component proof; not a surface classification or STCI theorem.'}
    (source.parent/'countercheck-result.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
