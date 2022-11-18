import discord
from discord.ext import commands
from discord.ext.commands import Bot

"""

Commandless bot that automatically publishes messages posted in news channels. [ ! UNTESTED ! ]

"""

intents = discord.Intents.default()
intents.messages = True

bot = Bot(intents=intents)

@bot.event
async def on_message(m):
    if m.author == bot.user or m.channel.isnews() == False: # check if the message is from this bot or from a news channel
      return # ignore if it isnt from a news channel or from this bot
  try:    
    await m.publish() # attempt to publish the message
  except discord.Forbidden as error: # bot doesn't have permission to publish (manage) messages
    print(error)
    try:
      await m.reply(content="**I was unable to publish this message; Missing `manage messages` permissions**")
    except discord.Forbidden: # at this point it is getting silly  
      print(f"Bot missing permissions to send messages in guild id {m.guild.id}")
  else:
    print("Published message!")
      
bot.run("token here")
