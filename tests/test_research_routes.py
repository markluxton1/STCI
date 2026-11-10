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
            compact = Repository(root).compact_route("sample")
            self.assertIn("Start — research/proof.md#scope", compact)
            self.assertIn("Proof — research/proof.md#proof", compact)
            self.assertNotIn("Hypothesis.", compact)
            self.assertNotIn("Proof text.", compact)
            selected = Repository(root).read_sections(["research/proof.md#proof"])
            self.assertIn("## Proof\n\nProof text.", selected)
            self.assertNotIn("Hypothesis.", selected)
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
            with self.assertRaisesRegex(ValueError, "missing fragment"):
                Repository(root).compact_route("sample")

    def test_section_ranges_are_disclosed_and_oversized_output_is_refused(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "owner.md").write_text("## Scope\n\nLine one.\nLine two.\n", encoding="utf-8")
            address = "owner.md#scope"
            output = Repository(root).read_sections([address], line_range=(3, 3))
            self.assertIn("Warning: partial source, showing lines 3–3 of 4.", output)
            self.assertIn("Line one.", output)
            self.assertNotIn("Line two.", output)
            with self.assertRaisesRegex(ValueError, "No source text was emitted"):
                Repository(root).read_sections([address], max_chars=40)
            with self.assertRaisesRegex(ValueError, "must lie within"):
                Repository(root).read_sections([address], line_range=(3, 5))
            with self.assertRaisesRegex(ValueError, "unsafe/nonlocal"):
                Repository(root).read_sections(["../owner.md#scope"])
