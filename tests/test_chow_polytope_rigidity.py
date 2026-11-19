"""Replay the H15 certificate in the existing research-infrastructure CI job."""
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / 'research/arguments/equations/chow_polytope_rigidity.support/verify.py'


class ChowPolytopeRigidityTests(unittest.TestCase):
    def test_integer_determinants_and_characteristic_free_faces(self):
        result = subprocess.run(
            [sys.executable, '-B', str(CHECKER)], cwd=ROOT,
            capture_output=True, text=True, check=True,
        )
        certificate = json.loads(result.stdout)
        self.assertEqual(certificate['status'], 'PASS')
        self.assertEqual(certificate['coefficient_ring'], 'Z')
        cases = certificate['cases']
        self.assertEqual([c['degree'] for c in cases], [1, 4, 4, 4])
        self.assertEqual([c['width_w2'] for c in cases], [0, 0, 0, 3])
        self.assertEqual([c['terms'] for c in cases], [2, 13, 13, 64])
        for case in cases:
            for witness in case['unit_witnesses']:
                self.assertEqual(abs(witness['coefficient']), 1)


if __name__ == '__main__':
    unittest.main()
