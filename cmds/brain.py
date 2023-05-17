import random
import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Brain(Cog_Extension):

    @commands.command()
    async def roll(self, ctx, number):
        member = ctx.author
        try:
            num = random.randint(1, int(number))
            await ctx.send(f"{member.mention} 結果是 {num}")
        except ValueError:
            await ctx.send("請輸入數字")
            
    @commands.command()
    async def password(self, ctx, number):
        try:
            member = ctx.author
            total = int(number) * 3
            times = total
            res = []

            if int(number) < 1 or int(number) > 9:
                await ctx.send("請輸入 1 ~ 9 的數字")
                return
            
            data = list(map(str, random.sample([i for i in range(10)], int(number))))
            message = await ctx.send(f"{member.mention} 歡迎來到1A2B，總共有{number}位數字")
            
            while times > 0:            
                A = 0
                B = 0
                try:
                    embed = discord.Embed(title="1A2B", description=f"```猜過的數字和結果會在這邊```")
                    for i in range(total - times):
                        embed.add_field(name=f"{res[i][0]}", value=f"```{res[i][1]}A{res[i][2]}B```", inline=False)
                    embed.add_field(name="剩餘次數",
                                    value=f"{times}", inline=False)

                    await message.edit(embed=embed)

                    num = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)

                    while not num.content.isdigit():
                        await ctx.send("請輸入 1 ~ 9 的數字")
                        num = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
                    while not len(num.content) == int(number):
                        await ctx.send(f"請輸入{number}位數字")
                        num = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
                    while not len(set(num.content)) == len(num.content):
                        await ctx.send(f"不會有重複的數字喔，債想想")
                        num = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
                except Exception as e:
                    await ctx.send(e)
                    await ctx.send("時間到，太慢囉!")
                    return 

                for i in range(len(num.content)):
                    if data[i] == num.content[i]:
                        A += 1
                    elif num.content[i] in data:
                        B += 1
                res.append([num.content, A, B])

                if A == int(number):
                    embed = discord.Embed(title="1A2B")
                    embed.description = f"{member.mention} 你猜中了! 數字是 {''.join(data)}"
                    embed.color = discord.Color.green()
                    await ctx.send(embed=embed)
                    return

                times -= 1
            else:
                embed = discord.Embed(title="1A2B")
                embed.description = f"猜不到是吧:confused: 答案是 {''.join(data)}"
                embed.color = discord.Color.red()
                await ctx.send(embed=embed)
                return
            
        except Exception as e:
            await ctx.send(e)

async def setup(bot):
    await bot.add_cog(Brain(bot))
