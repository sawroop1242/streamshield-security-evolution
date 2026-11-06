from html.parser import HTMLParser
from pathlib import Path
import unittest

FIXTURE = Path(__file__).parent / "fixtures" / "video-embed.html"
EXPECTED_SRC = "https://study-space.fembed.co/embed/PMmy_HJkq-N4n"
ALLOWED_HOST = "study-space.fembed.co"


class FixtureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.iframes = []
        self.scripts = 0
        self.inline_handlers = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag.lower() == "iframe":
            self.iframes.append(values)
        if tag.lower() == "script":
            self.scripts += 1
        self.inline_handlers.extend(k for k in values if k.lower().startswith("on"))


class VideoEmbedFixtureTests(unittest.TestCase):
    def test_fixture_contains_expected_authorized_embed(self):
        parser = FixtureParser()
        parser.feed(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(len(parser.iframes), 1)
        iframe = parser.iframes[0]
        self.assertEqual(iframe.get("src"), EXPECTED_SRC)
        self.assertEqual(iframe.get("title"), "StreamShield authorized video embed test")
        self.assertEqual(iframe.get("referrerpolicy"), "strict-origin-when-cross-origin")
        self.assertIn("allowfullscreen", iframe)
        self.assertEqual(iframe.get("allow"), "fullscreen")
        self.assertEqual(iframe.get("src", "").split("/")[2], ALLOWED_HOST)

    def test_fixture_has_no_scripts_or_inline_event_handlers(self):
        parser = FixtureParser()
        parser.feed(FIXTURE.read_text(encoding="utf-8"))
        self.assertEqual(parser.scripts, 0)
        self.assertEqual(parser.inline_handlers, [])


if __name__ == "__main__":
    unittest.main()
