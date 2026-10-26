#!/usr/bin/env python3
"""Persist execution and exact scope of the selected-carrier M2 certificate."""

from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import re
import subprocess
import time


HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
SOURCE = HERE / "endpoint4_fixed_m2_2026_10_25.m2"
FAMILY = HERE / "endpoint4_actual_2026_10_25.json"
OUT = HERE / "endpoint4_fixed_m2_2026_10_25.json"
LOG = HERE / "endpoint4_fixed_m2_2026_10_25.txt"
M2 = "/opt/homebrew/bin/M2"


def exponents(degree):
    return [[a, b, c, degree - a - b - c]
            for a in range(degree + 1)
            for b in range(degree - a + 1)
            for c in range(degree - a - b + 1)]


def main():
    family = json.loads(FAMILY.read_text())
    carrier = {}
    for key in ("a0", "constant", "kappa"):
        for term in family["ambient_parameter_blocks"][key]:
            exponent = tuple(term["exponents"])
            carrier[exponent] = carrier.get(exponent, Fraction(0)) + Fraction(term["coefficient"])
    carrier = {e: c for e, c in carrier.items() if c}
    degree6 = exponents(6)
    degree16 = exponents(16)
    assert len(degree6) == 84 and len(degree16) == 969
    assert all(sum(e) == 6 for e in carrier)

    started = datetime.now(timezone.utc).isoformat()
    timer = time.monotonic()
    result = subprocess.run([M2, "--script", str(SOURCE)], cwd=REPO,
                            text=True, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, timeout=180)
    elapsed = time.monotonic() - timer
    LOG.write_text(result.stdout)
    progression = [{"z": int(z), "rows": int(rows), "rank": int(rank)}
                   for z, rows, rank in re.findall(r"POINT=(\d+) ROWS=(\d+) RANK=(\d+)", result.stdout)]
    checks = [
        "ALL_30_SAMPLES_NONZERO_WITH_1_PLUS_Z_SQUARED_UNIT: PASS",
        "GLOBAL_MULTIPLES_RANK_286: PASS",
        "STACK_ANNIHILATES_ALL_286_GLOBAL_MULTIPLES: PASS",
        "FIXED_CARRIER_JET_KERNEL_EQUALS_MULTIPLES: PASS",
    ]
    passed = (result.returncode == 0 and len(progression) == 30
              and progression[-1] == {"z": 30, "rows": 690, "rank": 683}
              and all(check in result.stdout for check in checks)
              and "MULTIPLE_PRODUCT_RANK=0" in result.stdout)
    report = {
        "status": "PASS" if passed else "FAIL",
        "started_utc": started,
        "elapsed_seconds": elapsed,
        "command": [M2, "--script", str(SOURCE.relative_to(REPO))],
        "returncode": result.returncode,
        "script_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "family_json_sha256": hashlib.sha256(FAMILY.read_bytes()).hexdigest(),
        "log": str(LOG.relative_to(REPO)),
        "log_sha256": hashlib.sha256(LOG.read_bytes()).hexdigest(),
        "prime": 65521,
        "parameters": {"rho": -1, "a0": 1, "b1": 0, "b2": 0, "kappa": 1},
        "actual_carrier": "-q^2*x3^2-q*D*x2+D^2/4+q^3",
        "q": "x0*x3-x1*x2",
        "D": "x2^3-x1*x3^2",
        "normal_chart": "(1,z,z^3+v,z^4+u+(3/2)*z*v)",
        "necessary_condition": "G16 in (F6)+(u,v)^12 over QQ(z)[[u,v]]",
        "coefficient_unknowns": "all 969 global QQ coefficients; no QQ(z)-coefficient unknowns",
        "degree6_exponent_order": degree6,
        "degree6_carrier_coefficient_vector": [str(carrier.get(tuple(e), Fraction(0))) for e in degree6],
        "degree16_column_exponent_order": degree16,
        "sample_progression": progression,
        "truncated_jet_dimension": 78,
        "carrier_multiplication_rank_in_jet_space": 55,
        "sample_quotient_dimension": 23,
        "stacked_matrix_shape": [690, 969],
        "stacked_matrix_rank": 683 if passed else None,
        "global_degree10_multiples_dimension": 286,
        "global_multiples_matrix_shape": [969, 286],
        "global_multiples_rank": 286 if passed else None,
        "stack_times_global_multiples_rank": 0 if passed else None,
        "good_reduction": "All z=1..30 and z^2+1 are nonzero mod 65521; leading coefficient z^8*(1+z^2) is a unit",
        "characteristic_zero_consequence": "Necessary global jet kernel equals F6*H0(O_P3(10)) for this selected carrier, also after characteristic-zero field extension",
        "limitations": [
            "Only the displayed rho=-1,b2=0,kappa=1 carrier is tested",
            "No emptiness statement for the full endpoint-four chart",
            "No unrestricted STCI conclusion",
        ],
        "implementation_corrections_before_final_pass": [
            "Preserved nested exponent tuples instead of flattening all list levels",
            "Restored jetRing generators after each quotient-ring construction",
            "Wrapped multiline globalCarrier assignment in parentheses so all four terms are included",
            "Checked monomial-row permutation, ambient reconstruction, and annihilation explicitly",
        ],
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(result.stdout, end="")
    print(f"WROTE {OUT.relative_to(REPO)}")
    print(f"WROTE {LOG.relative_to(REPO)}")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
