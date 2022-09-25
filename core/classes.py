import discord
from discord.ext import commands

# set up class
class Cog_Extension(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
