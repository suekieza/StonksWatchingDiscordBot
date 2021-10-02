import discord
import os
bot_secret = os.environ['BOTTOKEN']


client = discord.Client()

@client.event
async def on_ready():
  print(f'We have logged in as {client}.user')

@client.event
async def on_massage(massage):
  if massage.author == client.user:
    return

  if massage.content.startswith('$hello'):
    await massage.channel.send('Hello')

client.run(bot_secret)