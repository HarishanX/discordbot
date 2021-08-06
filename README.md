# Discord bot to automate guild signup process

This bot will automate part of the joining process for any kind of guild. 

It consists on two main parts.

Given a message in a specific channel, from a specific user, it will add a custom set of (server specific) emoji as reaction on that message. 

The other part is, given an input message from a specific user or bot, it will process the given message and send a discord DM to the user with a predefined acceptance or rejection message. It will also send an error message on another channel if the bot is unable of sending the DM to the selected user, returning the input that failed. 

# REQUIREMENTS

Python3.5.2 or greater (for discord.py)
Discord.py 1.6 or greater
A Discord bot user with all intents unlocked (will need verification for usage on more that 100 servers) (TODO: check intent usage)

# HOW TO USE

v0.1: Replace all <> tagged content with the proper ID or text according to coments. 

# ROADMAP

v0.2: general ease of use and setup improvements