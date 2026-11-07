"""Positive and deliberately false controls for the toric finite checks."""
from pathlib import Path
import unittest


SOURCE = Path(__file__).with_name("verify.py")


def load_checks(source):
    namespace = {"__name__": "torus_residual_controls_test"}
    exec(compile(source, str(SOURCE), "exec"), namespace)
    return namespace


class VerifyControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")

    def rejects_mutation(self, group, original, altered, explanation):
        self.assertEqual(1, self.source.count(original), explanation)
        load_checks(self.source)[group]()
        bad_source = self.source.replace(original, altered, 1)
        with self.assertRaises(AssertionError, msg=explanation):
            load_checks(bad_source)[group]()

    def test_quotient_checks_reject_wrong_endpoint_coefficient(self):
        self.rejects_mutation(
            "quotient_checks",
            "a, b = [0, -3, 6, -10], [0, -4, 10, -20]",
            "a, b = [0, -3, 6, -11], [0, -4, 10, -20]",
            "Changing the quartic endpoint coefficient must break the checked quotient data.",
        )

    def test_jet_checks_reject_changed_jet_row_profile(self):
        self.rejects_mutation(
            "jet_checks",
            "mat = [[c[r] for c in columns] for r in range(3)]",
            "mat = [[c[r] for c in columns] for r in range(2)]",
            "Dropping a jet row changes the checked weight profile and source dimension.",
        )

    def test_residual_checks_reject_corrupted_actual_polynomial(self):
        self.rejects_mutation(
            "residual_checks",
            "f = add(power(qvar, 3), mul(power(h, 5), a6))",
            "f = add(power(qvar, 3), mul(power(h, 5), b4))",
            "Replacing the actual deformation polynomial factor must break its minor identity.",
        )

    def test_hilbert_checks_reject_incorrect_degree_sum(self):
        self.rejects_mutation(
            "hilbert_checks",
            "degree_sums == [36] * 9",
            "degree_sums == [37] * 9",
            "Changing the expected degree sum must fail the nine-cycle degree check.",
        )


if __name__ == "__main__":
    unittest.main()
