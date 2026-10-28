"""Dependency-free checks for the static portfolio's key requirements."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PortfolioParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.categories = []
        self.filters = []
        self.local_paths = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "article" and "card" in attrs.get("class", "").split():
            self.categories.append(attrs.get("data-cat"))
        if tag == "button" and "filter" in attrs.get("class", "").split():
            self.filters.append(attrs.get("data-f"))
        for key in ("src", "href"):
            value = attrs.get(key, "")
            if value and not value.startswith(("#", "http:", "https:", "mailto:", "tel:", "data:")):
                self.local_paths.append(value.split("#", 1)[0].split("?", 1)[0])


class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.parser = PortfolioParser()
        cls.parser.feed(cls.html)

    def test_one_sample_per_requested_category(self):
        expected = {"logo", "social", "thumb", "banner", "card", "print", "ui"}
        self.assertEqual(Counter(self.parser.categories), Counter({category: 1 for category in expected}))
        self.assertEqual(set(self.parser.filters), expected | {"all"})
        self.assertEqual(len(self.parser.filters), 8)
        self.assertNotIn("video", self.parser.categories)

    def test_local_assets_exist(self):
        missing = [path for path in self.parser.local_paths if not (ROOT / path).is_file()]
        self.assertEqual(missing, [])

    def test_palette_and_photos(self):
        css = (ROOT / "css/style.css").read_text(encoding="utf-8").upper()
        for color in ("#0B0B0D", "#171719", "#F5A623", "#FFC247", "#168BFF", "#F5F5F5", "#B8B8B8", "#34343A"):
            self.assertIn(color, css)
        for photo in ("noor-portrait.webp", "noor-about.webp", "noor-studio.webp"):
            self.assertIn(photo, self.html)

    def test_concepts_are_disclosed(self):
        self.assertIn("AI-generated concept previews", self.html)


if __name__ == "__main__":
    unittest.main()
