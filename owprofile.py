"""
api_v3 routes.
"""
import json

from blizz_interface import get_user_page
from parsing import *

def get_blob(filename: str):
    """
    Returns a giant blob of data.
    """
    page = get_user_page(filename)

    if page is None:
        return None

    built_dict = {"heroes": {"playtime": {"competitive": {}, "quickplay": {}},
                    "stats": {"competitive": {}, "quickplay": {}}},
            "stats": {},
            "achievements": {}}

    built_dict["stats"]["quickplay"] = bl_parse_stats(page)
    built_dict["stats"]["competitive"] = bl_parse_stats(page, mode="competitive")

    built_dict["heroes"]["stats"]["quickplay"] = bl_parse_hero_data(page)
    built_dict["heroes"]["playtime"]["quickplay"] = bl_parse_all_heroes(page)

    built_dict["heroes"]["stats"]["competitive"] = bl_parse_hero_data(page, mode="competitive")
    built_dict["heroes"]["playtime"]["competitive"] = bl_parse_all_heroes(page, mode="competitive")

    built_dict["achievements"] = bl_parse_achievement_data(page)

    return built_dict

def get_stats(filename: str):
    """
    Fetches stats about the user.
    """
    page = get_user_page(filename)

    if page is None:
        return None
        
    built_dict = {
        "stats": {},
    }

    built_dict["stats"]["quickplay"] = bl_parse_stats(page)
    built_dict["stats"]["competitive"] = bl_parse_stats(page, mode="competitive")

    return built_dict

def get_heroes(filename: str):
    """
    Fetches hero stats, in one big blob.
    """
    page = get_user_page(filename)

    if page is None:
        return None

    built_dict = {
        "heroes": {"playtime": {"competitive": {}, "quickplay": {}},
                    "stats": {"competitive": {}, "quickplay": {}}},
    }

    built_dict["heroes"]["stats"]["quickplay"] = bl_parse_hero_data(page)
    built_dict["heroes"]["playtime"]["quickplay"] = bl_parse_all_heroes(page)

    built_dict["heroes"]["stats"]["competitive"] = bl_parse_hero_data(page, mode="competitive")
    built_dict["heroes"]["playtime"]["competitive"] = bl_parse_all_heroes(page, mode="competitive")

    return built_dict


# Separate routes.
def get_heroes_qp(filename: str):
    """
    Fetches hero stats, for quick-play.
    """
    page = get_user_page(filename)

    if page is None:
        return None

    built_dict = {
        "heroes": {"playtime": {"competitive": {}, "quickplay": {}},
                    "stats": {"competitive": {}, "quickplay": {}}},
    }

    built_dict["heroes"]["stats"]["quickplay"] = bl_parse_hero_data(page)
    built_dict["heroes"]["playtime"]["quickplay"] = bl_parse_all_heroes(page)

    return built_dict

def get_heroes_comp(filename: str):
    """
    Fetches hero stats, for competitive.
    """
    page = get_user_page(filename)

    if page is None:
        return None

    built_dict = {
        "heroes": {
            "playtime":
                {
                    "competitive": {},
                    "quickplay": {}
                },
            "stats":
                {
                    "competitive": {},
                    "quickplay": {}
                }
        },
    }

    built_dict["heroes"]["stats"]["competitive"] = bl_parse_hero_data(page, mode="competitive")
    built_dict["heroes"]["playtime"]["competitive"] = bl_parse_all_heroes(page, mode="competitive")

    return built_dict

def get_achievements(filename: str):
    """
    Fetches hero stats, for competitive.
    """
    page = get_user_page(filename)

    if page is None:
        return None

    return {"achievements": bl_parse_achievement_data(page)}

