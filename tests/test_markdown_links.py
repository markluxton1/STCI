"""Small local-link controls; no network or research-file mutations."""
import importlib.util
from pathlib import Path
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_markdown_links.py"
spec = importlib.util.spec_from_file_location("markdown_links_under_test", SCRIPT)
links = importlib.util.module_from_spec(spec)
spec.loader.exec_module(links)


class MarkdownLinksTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.old_root = links.ROOT
        links.ROOT = self.root
        self.addCleanup(setattr, links, "ROOT", self.old_root)
        self.source = self.root / "source.md"
        (self.root / "target file.md").write_text(
            "# A title\n\n# A title\n\nSetext title\n============\n\n"
            '<a id="explicit"></a>\n\n```md\n# Hidden\n```\n', encoding="utf-8")

    def check(self, source, anchors=True):
        self.source.write_text(source, encoding="utf-8")
        return links.check_file(self.source, anchors)

    def test_valid_local_paths_fragments_and_external_citations(self):
        self.assertEqual([], self.check(
            "# Local\n[one](target%20file.md#a-title)\n"
            "[two](<target file.md#a-title-1>)\n"
            "[three](target%20file.md#setext-title)\n"
            "[four](target%20file.md#explicit)\n[here](#local)\n"
            "[ref]: target%20file.md#a-title\n"
            "[web](https://example.invalid/unfetched#anything)\n"))

    def test_broken_paths_and_anchors(self):
        for destination in ("missing.md", "target%20file.md#absent", "target%20file.md#hidden"):
            with self.subTest(destination=destination):
                errors = self.check(f"[bad]({destination})\n")
                self.assertTrue(errors, destination)
                self.assertTrue(all(isinstance(e, str) and e for e in errors))
        self.assertEqual([], self.check("[ignored fragment](target%20file.md#absent)", anchors=False))

    def test_fenced_examples_are_ignored_but_following_links_are_checked(self):
        for fence in ("```", "~~~~"):
            with self.subTest(fence=fence):
                example = f"{fence}markdown\n[example](missing.md)\n{fence}\n"
                self.assertEqual([], self.check(example))
                self.assertTrue(self.check(example + "[real](missing.md)\n"))

    def test_encoded_paths_and_symlinks_cannot_escape(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside).resolve() / "external.md"
            external.write_text("# Present\n", encoding="utf-8")
            (self.root / "escape.md").symlink_to(external)
            (self.root / "inside.md").symlink_to(self.root / "target file.md")
            self.assertEqual([], self.check("[inside](inside.md#a-title)"))
            relative = "../" + external.parent.name + "/external.md"
            for target in ("escape.md", relative, relative.replace("..", "%2e%2e")):
                with self.subTest(target=target):
                    self.assertTrue(self.check(f"[escape]({target})"), target)

    def test_frontmatter_and_code_do_not_supply_anchors(self):
        target = self.root / "metadata.md"
        target.write_text("---\ntitle: Fake\n---\n\n# Real\n", encoding="utf-8")
        self.assertEqual([], self.check("[real](metadata.md#real)"))
        self.assertTrue(self.check("[fake](metadata.md#title-fake)"))


if __name__ == "__main__":
    unittest.main()
