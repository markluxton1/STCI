import tempfile
import unittest
from pathlib import Path

from scripts.research import Repository


class ResearchRouteTests(unittest.TestCase):
    def test_resolves_index_sections_and_leaves_followup_unexpanded(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research = root / "research"
            research.mkdir()
            (research / "INDEX.md").write_text(
                "| `sample` | [Start](proof.md#scope) | [Proof](proof.md#proof) |\n",
                encoding="utf-8",
            )
            (research / "proof.md").write_text(
                "# Owner\n\n## Scope\n\nHypothesis.\n\n### Boundary\n\nBoundary text.\n"
                "\n## Proof\n\nProof text.\n",
                encoding="utf-8",
            )
            route = Repository(root).read_route("sample")
            self.assertIn("Source: research/proof.md#scope", route)
            self.assertIn("### Boundary\n\nBoundary text.", route)
            self.assertIn("[Proof](proof.md#proof)", route)
            self.assertNotIn("Proof text.", route)
            with self.assertRaisesRegex(ValueError, "Unknown research lane"):
                Repository(root).read_route("absent")

    def test_rejects_missing_section(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            research = root / "research"
            research.mkdir()
            (research / "INDEX.md").write_text(
                "| `sample` | [Start](proof.md#missing) | [Proof](proof.md#proof) |\n",
                encoding="utf-8",
            )
            (research / "proof.md").write_text("## Proof\n\nProof text.\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing fragment"):
                Repository(root).read_route("sample")
