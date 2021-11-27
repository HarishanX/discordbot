class token:
    BOT_TOKEN = ''              #Discord bot token

class emojis:
    emoji_accepted = ""         #emoji to display to accept user
    emoji_rejected = ""         #emoji to display to reject user
    channel_emoji = ""          #channel to react with emoji on
    author_emoji = ""           #author of the post to react

class messages:
    self_id = ""                #id of bot itself (used to avoid recursion)
    channel_trigger = ""        #if of channel where trigger message will be posted
    trigger_accepted = ""       #first part of message that will trigger the bot in case of aceptance
    trigger_rejected = ""       #first part of message that will trigger the bot in case of rejection
    splitter = "|"              #special character that will split the aceptance/rejected message
    clan_tag = ""               #tag to add to user nick/name in case of aceptance
    error_channel = ""          #id of channel to send errors to
    message_accepted = """ """  #full message to send on aceptance
    message_rejected = """ """  #full message to send on rejection