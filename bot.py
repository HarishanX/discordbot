import discord
from discord import message
from discord.ext    import commands
from discord.ext.commands   import Bot
from discord.ext.commands import MemberConverter
from discord.utils import get
from config import token
from config import emojis
from config import messages


intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print ("Running")

async def react(message):

    custom_emojis = [
    emojis.emoji_accepted, 
    emojis.emoji_rejected
    ]
    guild_emoji_names = [str(guild_emoji) for guild_emoji in message.guild.emojis]
    for emoji in custom_emojis:
        if emoji in guild_emoji_names:
            await message.add_reaction(emoji)

@bot.event
async def on_message(message):
    if str(message.channel.id) == emojis.channel_emoji and str(message.author.id) == emojis.author_emoji: 
        await react(message)

    if message.author.bot == False and message.author.id != messages.self_id:    
        if str(message.channel.id) == messages.channel_trigger:   
            if messages.trigger_accepted in message.content: 
                user= message.content.split(messages.splitter)
                clan = message.guild
                userid = clan.get_member_named(user[1])
                try:
                    await userid.send(messages.message_accepted)
                    if userid.nick:
                        if messages.clan_tag not in userid.nick:  
                            original = userid.nick
                            editado = messages.clan_tag + original
                            await userid.edit(nick=editado)
                    else:
                        original = userid.name
                        editado = messages.clan_tag + original
                        await userid.edit(nick=editado)
                except:
                    channel = bot.get_channel(messages.error_channel) 
                    await channel.send("Unable to send message to user {}.".format(user[1]) )

        if str(message.channel.id) == messages.channel_trigger:   
            if messages.trigger_rejected in message.content:  
                user= message.content.split(messages.splitter)
                clan = message.guild
                userid = clan.get_member_named(user[1])
                try:
                    await userid.send(messages.message_rejected)
                except:
                    channel = bot.get_channel(messages.error_channel) 
                    await channel.send("Unable to send message to user {}.".format(user[1]) )
    await bot.process_commands(message)


bot.run(token.BOT_TOKEN)
