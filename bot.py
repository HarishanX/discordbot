import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
from discord.ext.commands import MemberConverter
from discord.utils import get
import asyncio


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
#    guild = bot.get_guild('<GUILD_ID>')
    print ("Running")

async def react(message):

    custom_emojis = [
    "<:sipe:822053447200276491>", #personalized emoji code
    "<:nope:822053446814793729>"
    ]
    guild_emoji_names = [str(guild_emoji) for guild_emoji in message.guild.emojis]
    for emoji in custom_emojis:
        #print(emoji, guild_emoji_names)
        #print(emoji in guild_emoji_names)
        if emoji in guild_emoji_names:
            await message.add_reaction(emoji)

@bot.event
async def on_message(message):
    if str(message.channel.id) == "<CHANNEL_ID>" and str(message.author.id) == "<AUTHOR_ID>": #CHANNEL and AUTHOR of the message that has to be reacted
        await react(message)

    if message.author.bot and message.author.id != "<AUTHOR_ID>":    #Message author is a bot and not itself
        if str(message.channel.id) == "<CHANNEL_ID>":   #Message is on CHANNEL_ID channel
            if '<TRIGGER_SUCCESS>' in message.content: #TRIGGER must appear on message, inmediatly followed my SPLITTER
                user= message.content.split("<SPLITTER>")
                clan = message.guild
                userid = clan.get_member_named(user[1])
                try:
                    await userid.send("""<MESSAGE TO SEND ON SUCCESS>""")
                    if userid.nick:
                        if '<TAG>' not in userid.nick:  #TAG will be added to user name as nick
                            original = userid.nick
                            editado = "<TAG> " + original
                            await userid.edit(nick=editado)
                    else:
                        original = userid.name
                        editado = "<TAG> " + original
                        await userid.edit(nick=editado)
                except:
                    channel = bot.get_channel(<CHANNEL_ID>) #channel to send error message to
                    await channel.send("Unable to send message to user {}.".format(user[1]) )

        if str(message.channel.id) == "<CHANNEL_ID>":   #Message is on CHANNEL_ID channel
            if '<TRIGGER_FAILURE>' in message.content:  #TRIGGER must appear on message, inmediatly followed my SPLITTER
                user= message.content.split("<SPLITTER>")
                clan = message.guild
                userid = clan.get_member_named(user[1])
                try:
                    await userid.send("""MESSAGE TO SEND ON FAIL""")
                except:
                    channel = bot.get_channel(<CHANNEL_ID>) #channel to send error message to
                    await channel.send("Unable to send message to user {}.".format(user[1]) )
    await bot.process_commands(message)


bot.run("<BOT_TOKEN>")
