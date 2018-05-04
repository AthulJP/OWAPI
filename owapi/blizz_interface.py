"""
Interface that uses Blizzard's pages as the source.
"""
import functools

from lxml import etree

try:
    from html5_parser import parse
    _has_html5_parser = True
except ImportError:
    _has_html5_parser = False
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError

from owapi import util

# The currently available specific regions.


def get_page_body(filename: str) -> str:
    """
    Get HTML page body
    """

    page_file = open(filename, 'r')
    page_body = page_file.read()
    
    return page_body


def _parse_page_html5(content: str) -> etree._Element:
    """
    Internal function to parse a page and return the data.

    This uses html5_parser.
    """
    if content and content.lower() != 'none':
        data = parse(content)
        return data


def _parse_page_lxml(content: str) -> etree._Element:
    """
    Internal function to parse a page and return the data.

    This uses raw LXML.
    """
    if content and content.lower() != 'none':
        data = etree.HTML(content)
        return data


def get_user_page(filename: str) -> etree._Element:
    """
    Downloads the BZ page for a user, and parses it.
    """
    page_body = get_page_body(filename)

    if not page_body:
        return None

    # parse the page
    parsed = _parse_page(page_body)

    # sanity check
    node = parsed.findall(".//section[@class='u-nav-offset']//h1[@class='u-align-center']")
    for nodes in node:
        if nodes.text.strip() == "Profile Not Found":
            return None

    return parsed


if _has_html5_parser:
    _parse_page = _parse_page_html5
else:
    _parse_page = _parse_page_lxml
