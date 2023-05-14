import json
from discord.ext import commands
from core.classes import Cog_Extension


with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Word(Cog_Extension):
    @commands.command()
    async def Pneumonoultramicroscopicsilico_volcanoconiosis(self, ctx):
        member = ctx.author
        await ctx.send(member.mention + " " + jdata["火山矽肺症"])

    @commands.command()
    async def Floccinaucinihilipilification(self, ctx):
        member = ctx.author
        await ctx.send(member.mention + " " + jdata["蔑視"])

    @commands.command()
    async def Antidisestablishmentarianism(self, ctx):
        member = ctx.author
        await ctx.send(member.mention + " " + jdata["反政教分離"])

    @commands.command()
    async def Humuhumu_nukunuku_a_pua_a(self, ctx):
        member = ctx.author
        await ctx.send(member.mention + " " + jdata["斜帶吻棘魨"])

    @commands.command()
    async def Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch(self, ctx):
        member = ctx.author
        await ctx.send(member.mention + " " + jdata["蘭韋爾普爾古因吉爾戈格里惠爾恩德羅布爾蘭蒂西利奧戈戈戈赫"])


async def setup(bot):
    await bot.add_cog(Word(bot))
