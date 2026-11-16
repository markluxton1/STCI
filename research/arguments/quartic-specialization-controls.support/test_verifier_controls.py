"""Positive and deliberately corrupted controls for the four exact replays."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


HERE = Path(__file__).resolve().parent


class VerifierControls(unittest.TestCase):
    def check_pair(self, filename, command, original_datum, false_datum, rejection):
        source = HERE / filename
        original = source.read_text(encoding="utf-8")
        self.assertEqual(original.count(original_datum), 1)
        positive = subprocess.run(
            [*command, str(source)], text=True, capture_output=True, timeout=120,
        )
        self.assertEqual(positive.returncode, 0, positive.stdout + positive.stderr)

        with tempfile.TemporaryDirectory(prefix="stci-quartic-control-") as tmp:
            changed = Path(tmp) / filename
            changed.write_text(
                original.replace(original_datum, false_datum), encoding="utf-8",
            )
            negative = subprocess.run(
                [*command, str(changed)], text=True, capture_output=True, timeout=120,
            )
        self.assertNotEqual(negative.returncode, 0, "false datum was accepted")
        self.assertIn(rejection, negative.stderr, negative.stdout + negative.stderr)

    def test_normal_bundle_python(self):
        self.check_pair(
            "verify_normal_bundle.py",
            [sys.executable],
            "[-4 * u**-7, 3 * u**-8]",
            "[-4 * u**-7, 4 * u**-8]",
            "assert sp.simplify(transition - expected) == sp.zeros(2)",
        )

    def test_symbol_comparison_python(self):
        self.check_pair(
            "verify_44_quartic_symbol_comparison_2026_10_23.py",
            [sys.executable],
            "assert rank(m0)==17",
            "assert rank(m0)==18",
            "assert rank(m0)==18",
        )

    def test_session_normal_bundle_m2(self):
        self.check_pair(
            "verify_session_quartic_normal_bundle_2026_10_10.m2",
            ["M2", "--script"],
            "abs(det Q) == 2^15",
            "abs(det Q) == 2^14",
            "FAILED: quadratic syzygy coefficient determinant",
        )

    def test_mu4_m2(self):
        self.check_pair(
            "verify_44_mu4_family_2026_10_23.m2",
            ["M2", "--script"],
            "ideal(F2,G2) == ideal(X,Y^4)",
            "ideal(F2,G2) == ideal(X,Y^3)",
            "error: assertion failed",
        )
