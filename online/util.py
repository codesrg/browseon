from __future__ import annotations

import urllib.request
from srutil import util
from pathlib import Path
from urllib.parse import urlparse
from configparser import ConfigParser


class OnlineException(Exception):
    pass


def encoded_query(_query: str) -> str:
    replaces = {'%': '%25', ':': '%3A', ';': '%3B', '@': '%40', '#': '%23', '$': '%24', '=': '%3D', ',': '%2C',
                '?': '%3F', '/': '%2F', '&': '%26', '+': '%2B', ' ': '+'}
    query = ''
    for letters in _query:
        query += replaces.get(letters) if letters in replaces else letters
    return query


def get_baseurl_for(web_engine: str) -> str:
    ini_path = Path(__file__ + "/../config/config.ini").absolute()
    engine = config(ini_path, "web-engine")
    base_url = util.stringbuilder(engine.get("base-url"), "/?",
                                  config(ini_path, "url-param", "base-url"), "=",
                                  engine.get(web_engine))
    return base_url


def is_valid_url(url: str) -> bool:
    if util.isnetworkconnected():
        result = urlparse(url)
        response = urllib.request.urlopen(url)
        return all([result.scheme, result.netloc, result.path]) and response.code < 400
    else:
        raise OnlineException("Invalid URL.")


def config(file, section, key=None) -> dict | str:
    parser = ConfigParser()
    parser.read(file)
    items = dict(parser.items(section))
    if key:
        return items.get(key)
    return items
