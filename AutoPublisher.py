import discord
from discord.ext.commands import Bot

"""
Commandless bot that automatically publishes messages posted in announcements channels.
"""

intents = discord.Intents.default()

bot = Bot(intents=intents, command_prefix=".")

@bot.event
async def on_message(m):
    if m.channel.is_news():  # checks if channel is an announcements channel.
            if m.author == bot.user:  # check if the message is from this bot
                return  # return if the message was from a bot.
            try:
                await m.publish()  # publish the message
            except discord.Forbidden:  # bot doesn't have permission to publish (manage) messages
                print("Does not have manage messages permission")

            else:
                print("Published message!")
bot.run("token here")
