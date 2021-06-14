import discord
from discord.ext import commands
from discord.flags import MemberCacheFlags

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='-',intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(504579972934139919)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(504579972934139919)
    await channel.send(f'{member} leave!')

bot.run('ODUzOTU4NzM2NTY1NTAxOTcy.YMc9DA.zVu91n7wQY5xZERZU0Fg45MdiF4')
