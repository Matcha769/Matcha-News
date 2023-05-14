import random
import json
from discord.ext import commands
from core.classes import Cog_Extension


with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def cat(self, ctx):
        rp = random.choice(jdata["cat"])
        await ctx.send(rp)

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clear(self, ctx, num: int):
        await ctx.channel.purge(limit=num + 1)

    @commands.command()
    async def meal(self, ctx):
        chose = random.choice(jdata["午餐選擇"])
        await ctx.send(f"我覺得{chose}比較好!")


async def setup(bot):
    await bot.add_cog(React(bot))
