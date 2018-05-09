## OWProfile

[Donate to keep OWAPI alive, this is pretty much 99% their work](https://www.patreon.com/sundwarf)

This is a fork of https://github.com/Fuyukai/OWAPI but basically just cut down to work as a module that you can import rather than run as a REST API.

## Other differences from OWAPI

* This library doesn't have any functions to retrieve information about the heroes themselves. 
* `get_stats()` returns both hero stats (including playtime) and gamemode-specific stats
* Requires that you download the HTML page of the player whose data you want, this is so you can use whatever external tool you want to handle the downloads.
* No asyncio. No idea if you can run this in parallel somehow but I don't really care.
* No regions or platforms. No idea if this works with Xbox/Playstation, if it doesn't feel free to notify me or send a pull request.

## Game data

This API does not aim to expose data about the heroes, maps, etc in the game. For that, use 
https://github.com/jamesmcfadden/overwatch-api. 

It basically just returns the same stuff as OWAPI so if you want to see what you're getting just look here: https://github.com/Fuyukai/OWAPI/blob/master/api.md

I do have something in mind to fix getting the correct level as prestiges + level don't accurately reflect the level of a player who is level 1800+, but I don't know if I'll get around to that.
 
## API Docs

OWProfile functions return JSON dicts.   
 
**Installation steps:**

 1. **Clone the repository.**
 
     `git clone https://github.com/SunDwarf/OWAPI.git`
     
 2. **Install the requirements.**

     For debian-based systems, run this first:
        `sudo apt install libxslt-dev python3-dev build-essential zlib1g-dev pkg-config`

     To set up the virtualenv:
     `pipenv install`

 3. **Import owprofile.**
    `import owprofile *`

