import discord
import random
from discord.ext import commands
from core.classes import Cog_Extension
import time

class Game(Cog_Extension):
    
    @commands.command()
    async def gn(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        answer = list(range(1, 1000))
        number = random.choice(answer)
        member = ctx.author
        await ctx.send('請輸入數字(1~1000)')
        try:
            for i in range(0, 10):    
                response = await self.bot.wait_for('message',check = check)
                guess = int(response.content)
                await ctx.channel.purge(limit=2)
                if guess > number and i <= 8:
                    await ctx.send(f'{member.mention}再小一點')
                elif guess < number and i <= 8:
                    await ctx.send(f'{member.mention}再大一點')
                elif guess == number:
                    await ctx.send(f'{member.mention}答對了')
                    break
            else:
                await ctx.send("時辰已過，請擇日再戰:rolling_eyes:")        
        except:
          await ctx.send("輸入錯誤，請重新輸入指令")

    @commands.command()
    async def choose(self, ctx, *args):
        chose = random.choice(args)
        response = [f"我覺得{chose}比較好!",f"{chose}看起來比較合理",f"絕對是{chose}了吧"]
        await ctx.send(random.choice(response))
    @commands.command()
    async def vote(self, ctx, *args):
        question = args[0]
        choices = args[1:]
        await ctx.message.delete()
        await ctx.send(f":bar_chart:{question}")
        embed = discord.Embed(colour=discord.Colour(0xf1c40f))
        emoji = {0:"1️⃣",1:"2️⃣",2:"3️⃣",3:"4️⃣",4:"5️⃣",5:"6️⃣",6:"7️⃣"}
        for i in range(len(choices)):
            embed.add_field(name=f"{emoji[i]}", value=f"{choices[i]}", inline=True)
        msg = await ctx.send(embed = embed)
        for i in range(len(choices)):
            await msg.add_reaction(f"{emoji[i]}")
    
    @commands.command()
    async def coin(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        while True:
            coins = ["正面","反面"]
            result = random.choice(coins)
            await ctx.send('請輸入:正面 or 反面')
            try:
                response = await self.bot.wait_for('message', check = check)
                while response.content not in coins:
                    await ctx.send("輸入:正面 or 反面")
                    response = await self.bot.wait_for('message', check = check)
                guess = response.content
                if result == guess:
                    await ctx.send("猜對囉")
                elif result != guess:
                    await ctx.send("你猜錯了")
                time.sleep(1)
                await ctx.send("還要在玩一次嗎? (yes/no)")
                play_again = await self.bot.wait_for('message', check = check)
                if play_again.content.lower() != "yes":
                    await ctx.send("真的不玩了嗎!? 好吧")
                    break
            except:
                await ctx.send("輸入錯誤，請重新輸入指令")
                break
 
    @commands.command()
    async def daily(self, ctx, *goal):
        member = ctx.author
        data = ["小吉","中吉","大吉","吉","末吉","凶","大凶"]
        response = random.choices(data , weights =[40,30,5,20,50,10,5])
        answer , thing = "".join(response) , "".join(goal)
        if thing == "":
            await ctx.send(f'{member.mention} 【今日運氣預測】: ||{answer}||')
        else:
            for i in goal:
                response = random.choices(data , weights =[40,30,5,20,50,10,5])
                answer = "".join(response)
                await ctx.send(f'{member.mention} 【{i}運氣預測】: ||{answer}||')

    @commands.command()
    async def rps(self, ctx):
        a = ["石頭", "剪刀", "布"]
        start = [
            ":crossed_swords: 來決鬥吧:crossed_swords: ", "區區一介凡人也妄想挑戰本喵:smirk: ",
            "就給你一個挑戰的機會吧:rolling_eyes: "
        ]
        draw = [
            "本喵不過放水罷了:yawning_face: ", "竟然有和本喵相同的水準:face_with_raised_eyebrow: "
        ]
        win = [
            "甚麼:interrobang: 竟然被打敗了", "不過僥倖被你贏了一次:triumph: ",
            "能夠贏過本喵，享受無上榮耀吧:unamused: "
        ]
        lose = [
            "正常發揮罷了", "你想贏我先去練個800年吧", "失敗是對你的憐憫",
            ":place_of_worship: 膜拜本喵吧:place_of_worship: "
        ]
        msg1 = None

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        while True:
            answer = random.choice(a)
            await ctx.send(random.choice(start))
            time.sleep(1)
            await ctx.send("輸入:剪刀 or 石頭 or 布")
            time.sleep(1)
            msg1 = await self.bot.wait_for('message', check=check)
            while msg1.content not in a:
                await ctx.send("輸入:剪刀 or 石頭 or 布")
                time.sleep(1)
                msg1 = await self.bot.wait_for('message', check=check)
            msg = msg1.content
            await ctx.send("本喵出的是:" + answer)
            time.sleep(1)
            if msg == answer:
                await ctx.send("平手")
                time.sleep(1)
                await ctx.send(random.choice(draw))
            elif msg == "石頭" and answer == "剪刀":
                await ctx.send("你贏了")
                time.sleep(1)
                await ctx.send(random.choice(win))
            elif msg == "石頭" and answer == "布":
                await ctx.send("你輸了")
                time.sleep(1)
                await ctx.send(random.choice(lose))
            elif msg == "剪刀" and answer == "布":
                await ctx.send("你贏了")
                time.sleep(1)
                await ctx.send(random.choice(win))
            elif msg == "剪刀" and answer == "石頭":
                await ctx.send("你輸了")
                time.sleep(1)
                await ctx.send(random.choice(lose))
            elif msg == "布" and answer == "石頭":
                await ctx.send("你贏了")
                time.sleep(1)
                await ctx.send(random.choice(win))
            elif msg == "布" and answer == "剪刀":
                await ctx.send("你輸了")
                time.sleep(1)
                await ctx.send(random.choice(lose))
            time.sleep(1)
            await ctx.send("還要在玩一次嗎? (yes/no)")
            play_again = await self.bot.wait_for('message', check=check)
            if play_again.content.lower() != "yes":
                await ctx.send("真的不玩了嗎!? 好吧")
                break

def setup(bot):
    bot.add_cog(Game(bot))