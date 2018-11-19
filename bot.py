# Start date November 17th, 2018
# Python v3.6

import json
import discord
from discord.ext import commands

# Ignore the following commented out code. Mods are discussing how we will handle hosting and the bot's token.

# cacheJSON = 'json/cache.json'

# try:
#     with open(cacheJSON, 'r') as foo:
#         contents = json.load(foo)
#         TOKEN = contents['token']

# except FileNotFoundError:
#     pass

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    async def on_message(self, message):
        if message.author.bot or message.author == self.user:
            return
        
        await self.process_commands(message)

bot = Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as: ')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
@bot.command()
async def hello(ctx):
    """
    If a user types !hello the bot will respond with 'Hello! (nameOfUser here)
    """
    await ctx.send(f"Hello! {ctx.author.mention}")

bot.run(TOKEN)
