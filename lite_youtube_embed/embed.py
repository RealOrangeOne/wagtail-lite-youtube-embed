import re
from typing import Any, Dict, List, Optional

from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from wagtail.embeds.finders.oembed import OEmbedFinder
from wagtail.embeds.oembed_providers import youtube


class LiteYouTubeEmbedFinder(OEmbedFinder):
    """
    A modified OEmbed finder uses lite-youtube-embed instead

    https://github.com/paulirish/lite-youtube-embed
    """

    VIDEO_ID_RE = re.compile(r"\/embed\/([a-zA-Z0-9_-]+?)\?")

    def __init__(
        self, providers: Optional[List[Dict]] = None, options: Optional[Dict] = None
    ):
        super().__init__(providers=[youtube], options=options)

        self.params = options.get("params", {}) if options else {}

    @classmethod
    def _get_video_id(cls, html: str) -> str:
        matched = cls.VIDEO_ID_RE.search(html)
        if matched is None:
            raise ValueError(f"Unable to find video id in {html}")
        return matched.group(1)

    def find_embed(self, *args: Any, **kwargs: Any) -> Dict:
        result = super().find_embed(*args, **kwargs)
        video_id = self._get_video_id(result["html"])

        attrs = {
            "videoid": video_id,
            "title": result["title"],
            "backgroundImage": result["thumbnail_url"],
            **self.params,
        }

        result["html"] = mark_safe(f"<lite-youtube{flatatt(attrs)}></lite-youtube>")

        return result
