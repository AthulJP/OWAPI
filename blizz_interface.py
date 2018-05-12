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

def parse_page_html5(content: str) -> etree._Element:
    """
    Internal function to parse a page and return the data.

    This uses html5_parser.
    """
    if content and content.lower() != 'none':
        data = parse(content)
        return data


def parse_page_lxml(content: str) -> etree._Element:
    """
    Internal function to parse a page and return the data.

    This uses raw LXML.
    """
    if content and content.lower() != 'none':
        data = etree.HTML(content)
        return data


def get_user_page(page_text: str) -> etree._Element:
    """
    Takes the contents of the HTML file and parses it, pass this to the data parsing functions.
    """
    # parse the page
    user_page = parse_page(page_text)

    # sanity check
    node = user_page.findall(".//section[@class='u-nav-offset']//h1[@class='u-align-center']")
    for nodes in node:
        if nodes.text.strip() == "Profile Not Found":
            return None

    return user_page


if _has_html5_parser:
    parse_page = parse_page_html5
else:
    parse_page = parse_page_lxml
