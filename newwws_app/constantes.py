#!/usr/bin/python3
# -*- coding: Utf-8 -*

from stop_words import get_stop_words


# everything API news
SORTBY = ['elevancy', 'popularity', 'publishedAt']

# headlines API news
CATEGORIES = ['business', 'entertainment', 'generalhealth', 'science', 'sports', 'technology']
COUNTRIES = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cu', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'si', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']

# both API news
LANGUAGES = ['ar', 'de', 'en', 'es', 'fr', 'he', 'it', 'nl', 'pt', 'ru', 'se', 'zh']

# parseMode
STOP_WORDS = get_stop_words('en') + get_stop_words('fr')
NO_CHARS_LIST = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    ";",
    ":",
    ",",
    ".",
    "/",
    "<",
    ">",
    "?",
    "|",
    "`",
    "~",
    "-",
    "=",
    "_",
    "+",
    "&",
    "'",
    "§",
    "°",
    "^",
    "¨",
    "%",
    "`",
    "£",
    "-",
    "_",
]
