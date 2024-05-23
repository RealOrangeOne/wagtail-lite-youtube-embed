from django.test import SimpleTestCase
from wagtail.embeds.finders import get_finders
from wagtail.embeds.finders.oembed import OEmbedFinder

from lite_youtube_embed import LiteYouTubeEmbedFinder


class YouTubeLiteEmbedFinderTestCase(SimpleTestCase):
    def test_finds_video_id(self) -> None:
        self.assertEqual(
            LiteYouTubeEmbedFinder._get_video_id(
                '<iframe width="200" height="113" src="https://www.youtube.com/embed/dQw4w9WgXcQ?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen title=""></iframe>'
            ),
            "dQw4w9WgXcQ",
        )
        with self.assertRaises(ValueError):
            LiteYouTubeEmbedFinder._get_video_id("something-else")

    def test_uses_lite_youtube(self):
        self.assertIn(
            "</lite-youtube>",
            LiteYouTubeEmbedFinder().find_embed(
                "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            )["html"],
        )

    def test_in_finders(self):
        self.assertIsInstance(get_finders()[0], LiteYouTubeEmbedFinder)

    def test_reject_other_embed(self):
        self.assertFalse(
            LiteYouTubeEmbedFinder().accept(
                "https://open.spotify.com/track/4PTG3Z6ehGkBFwjybzWkR8"
            )
        )
        self.assertTrue(
            OEmbedFinder().accept(
                "https://open.spotify.com/track/4PTG3Z6ehGkBFwjybzWkR8"
            )
        )
