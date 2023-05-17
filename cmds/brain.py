import random
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
            guessed = False
            times = int(number) * 3

            if int(number) < 1 or int(number) > 9:
                await ctx.send("請輸入 1 ~ 9 的數字")
                return
            
            data = list(map(str, random.sample([i for i in range(10)], int(number))))
            await ctx.send(f"{member.mention} 歡迎來到1A2B，總共有{number}位數字")
            
            while not guessed and times > 0:            
                A = 0
                B = 0
                try:
                    await ctx.send(f"請輸入你的數字 (還有{times}次機會)")
                    num = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
                    while not num.content.isdigit():
                        await ctx.send("請輸入 1 ~ 9 的數字")
                        num = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
                    while not len(num.content) != len(number):
                        await ctx.send(f"請輸入{number}位數字")
                        num = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
                except:
                    await ctx.send("時間到，太慢囉!")
                    return 

                for i in range(len(num.content)):
                    if data[i] == num.content[i]:
                        A += 1
                    elif num.content[i] in data:
                        B += 1
                await ctx.send(f"{member.mention} {num.content} 的結果是{A}A{B}B")

                if A == int(number):
                    guessed = True
                    await ctx.send(f"{member.mention} 你猜中了! 數字是 {''.join(data)}")
                    return

                times -= 1
            else:
                await ctx.send(f"猜不到是吧:confused: 答案是 {''.join(data)}")
        except Exception as e:
            await ctx.send(e)

async def setup(bot):
    await bot.add_cog(Brain(bot))
