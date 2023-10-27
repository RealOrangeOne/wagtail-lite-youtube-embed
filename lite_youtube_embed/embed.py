import re
from typing import Dict, List, Optional

from django.utils.html import format_html
from wagtail.embeds.finders.oembed import OEmbedFinder
from wagtail.embeds.oembed_providers import youtube


class LiteYouTubeEmbedFinder(OEmbedFinder):
    """
    A modified OEmbed finder uses lite-youtube-embed instead

    https://github.com/paulirish/lite-youtube-embed
    """

    EMBED_ID_RE = re.compile(r"\/embed\/(.*?)\?")

    def __init__(
        self, providers: Optional[List[Dict]] = None, options: Optional[Dict] = None
    ):
        super().__init__(providers=[youtube], options=options)

    @classmethod
    def _get_video_id(cls, html: str) -> str:
        matched = cls.EMBED_ID_RE.search(html)
        if matched is None:
            raise ValueError(f"Unable to find video id in {html}")
        return matched.group(1)

    def find_embed(self, *args: List, **kwargs: Dict) -> Dict:
        result = super().find_embed(*args, **kwargs)
        video_id = self._get_video_id(result["html"])
        result["html"] = format_html(
            "<lite-youtube videoid='{}' playlabel='{}' backgroundImage='{}'></lite-youtube>",
            video_id,
            result["title"],
            result["thumbnail_url"],
        )
        return result
