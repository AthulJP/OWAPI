"""
api_v3 routes.
"""
import json

from owapi.blizz_interface import get_user_page
from owapi.blizz_interface import get_all_heroes
from owapi.blizz_interface import get_hero_data
from owapi.v3 import parsing


def get_blob(filename: str):
    """
    Returns a giant blob of data.
    """
    pages = get_user_page(filename)

    built_dict = {}
    for region, result in pages.items():
        if result is None:
            built_dict[region] = None
            continue
        d = {"heroes": {"playtime": {"competitive": {}, "quickplay": {}},
                        "stats": {"competitive": {}, "quickplay": {}}},
             "stats": {},
             "achievements": {}}

        d["stats"]["quickplay"] = parsing.bl_parse_stats(result)
        d["stats"]["competitive"] = parsing.bl_parse_stats(result, mode="competitive")

        d["heroes"]["stats"]["quickplay"] = parsing.bl_parse_hero_data(result)
        d["heroes"]["playtime"]["quickplay"] = parsing.bl_parse_all_heroes(result)

        d["heroes"]["stats"]["competitive"] = parsing.bl_parse_hero_data(result, mode="competitive")
        d["heroes"]["playtime"]["competitive"] = parsing.bl_parse_all_heroes(result,
                                                                             mode="competitive")

        d["achievements"] = parsing.bl_parse_achievement_data(result)

        built_dict[region] = d

    return built_dict

def get_stats(filename: str):
    """
    Fetches stats about the user.
    """
    pages = await get_user_page(filename)

    built_dict = {}
    for region, result in pages.items():
        if result is None:
            built_dict[region] = None
            continue
        d = {
            "stats": {},
        }

        d["stats"]["quickplay"] = parsing.bl_parse_stats(result)
        d["stats"]["competitive"] = parsing.bl_parse_stats(result, mode="competitive")

        built_dict[region] = d

    return built_dict

def get_heroes(filename: str):
    """
    Fetches hero stats, in one big blob.
    """
    pages = await get_user_page(filename)

    built_dict = {}
    for region, result in pages.items():
        if result is None:
            built_dict[region] = None
            continue
        d = {
            "heroes": {"playtime": {"competitive": {}, "quickplay": {}},
                       "stats": {"competitive": {}, "quickplay": {}}},
        }

        d["heroes"]["stats"]["quickplay"] = parsing.bl_parse_hero_data(result)
        d["heroes"]["playtime"]["quickplay"] = parsing.bl_parse_all_heroes(result)

        d["heroes"]["stats"]["competitive"] = parsing.bl_parse_hero_data(result, mode="competitive")
        d["heroes"]["playtime"]["competitive"] = parsing.bl_parse_all_heroes(result,
                                                                             mode="competitive")

        built_dict[region] = d

    return built_dict


# Separate routes.
def get_heroes_qp(filename: str):
    """
    Fetches hero stats, for quick-play.
    """
    pages = get_user_page(filename)

    built_dict = {}
    for region, result in pages.items():
        if result is None:
            built_dict[region] = None
            continue
        d = {
            "heroes": {"playtime": {"competitive": {}, "quickplay": {}},
                       "stats": {"competitive": {}, "quickplay": {}}},
        }

        d["heroes"]["stats"]["quickplay"] = parsing.bl_parse_hero_data(result)

        d["heroes"]["playtime"]["quickplay"] = parsing.bl_parse_all_heroes(result)

        built_dict[region] = d

    return built_dict

def get_heroes_comp(filename: str):
    """
    Fetches hero stats, for competitive.
    """
    pages = get_user_page(filename)

    built_dict = {}
    for region, result in pages.items():
        if result is None:
            built_dict[region] = None
            continue
        d = {
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

        d["heroes"]["stats"]["competitive"] = parsing.bl_parse_hero_data(result, mode="competitive")

        d["heroes"]["playtime"]["competitive"] = parsing.bl_parse_all_heroes(result,
                                                                             mode="competitive")

        built_dict[region] = d

    return built_dict

def get_achievements(filename: str):
    """
    Fetches hero stats, for competitive.
    """
    pages = get_user_page(filename)

    built_dict = {}
    for region, result in pages.items():
        if result is None:
            built_dict[region] = None
            continue
        d = {"achievements": parsing.bl_parse_achievement_data(result)}

        built_dict[region] = d

    return built_dict


async def get_hero_list(filename: str):
    """
    Send hero list.
    """
    parsed = get_user_page(filename)
    heroes = parsing.bl_get_all_heroes(parsed)

    built_dict = {"Offense": {}, "Defense": {}, "Tank": {}, "Support": {}}
    for hero in heroes:
        _parsed = await get_user_page(ctx, hero.lower())
        retHero = parsing.bl_find_heroes(_parsed)
        built_dict[retHero["role"]][hero] = retHero

    return built_dict

async def get_hero(filename: str, hero: str):
    """
    Send hero data for selected hero.
    """
    parsed = get_user_page(filename)
    _hero = parsing.bl_find_heroes(parsed)
    _hero["name"] = hero
    return _hero


get_achievements.should_convert = False
