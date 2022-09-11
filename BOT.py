from asyncio.tasks import wait
import discord
import random
from discord.ext import commands, tasks
from random import choice
import json
import os
import time
import keep_alive

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='-', intents=intents, help_command=None)


@bot.event
async def on_ready():
    activity = discord.Game(name="勥烎菿奣", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print(">> Bot is online <<")


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    i, ma, se = "\u3044", "\u307e", "\u305b"
    if "詩音" in message.content and not (message.author.bot):
        channel = message.channel
        member = message.author
        await channel.send(f'{member.mention} {i}{ma}幸{se}?')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'卸載[{extension}]成功')


@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'重載[{extension}]成功')


@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'載入[{extension}]成功')


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

keep_alive.keep_alive()

if __name__ == "__main__":
  try:
    bot.run(jdata['TOKEN'])
  except:
    os.system("kill 1")