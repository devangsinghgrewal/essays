#!/usr/bin/env python
AUTHOR = "Devang Grewal"
SITENAME = "Devang Grewal"
SITESUBTITLE = "Essays on AI, programming and life"
SITEURL = ""  # Empty for development; set in publishconf.py

PATH = "content"
TIMEZONE = "Asia/Kolkata"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None

# Theme settings
THEME = "theme"
DEFAULT_PAGINATION = 10
TYPOGRIFY = True

# URL settings
ARTICLE_URL = "{date:%Y}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

# Plugins (empty for now; add later if needed)
PLUGINS: list[str] = []

# Static paths (images, extra files like favicon)
STATIC_PATHS = ["images", "extra"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path": "favicon.ico"},
}

# Provide current time function to templates
import datetime
JINJA_GLOBALS = {
    "now": datetime.datetime.utcnow,
} 