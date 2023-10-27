# Wagtail Lite YouTube Embed

![CI](https://github.com/RealOrangeOne/wagtail-lite-youtube-embed/workflows/CI/badge.svg)
![PyPI](https://img.shields.io/pypi/v/wagtail-lite-youtube-embed.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wagtail-lite-youtube-embed.svg)
![PyPI - License](https://img.shields.io/pypi/l/wagtail-lite-youtube-embed.svg)

A Wagtail embed finder to use [`lite-youtube`](https://github.com/paulirish/lite-youtube-embed) for more efficient and private YouTube embeds.

## Installation

```
pip install wagtail-lite-youtube-embed
```

Then, configure `WAGTAILEMBEDS_FINDERS` to use `LiteYouTubeEmbedFinder` before the default OEmbed finder:

```python
WAGTAILEMBEDS_FINDERS = [
    {
        "class": "lite_youtube_embed.LiteYouTubeEmbedFinder",
    },
    {
        "class": "wagtail.embeds.finders.oembed",
    },
]
```

Note: This library does not configure your frontend to use `lite-youtube` - you will need to install and load this yourself.
