import discord
import random
import json
import time
from interactions import Button, spread_to_rows
from discord.ext import commands
from core.classes import Cog_Extension


with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Game(Cog_Extension):
    @commands.command()
    async def gn(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        answer = list(range(1, 1000))
        number = random.choice(answer)
        member = ctx.author
        await ctx.send("請輸入數字(1~1000)")
        try:
            for i in range(0, 10):
                response = await self.bot.wait_for("message", check=check)
                guess = int(response.content)
                await ctx.channel.purge(limit=2)
                if guess > number and i <= 8:
                    await ctx.send(f"{member.mention}再小一點")
                elif guess < number and i <= 8:
                    await ctx.send(f"{member.mention}再大一點")
                elif guess == number:
                    await ctx.send(f"{member.mention}答對了")
                    break
            else:
                await ctx.send("時辰已過，請擇日再戰:rolling_eyes:")
        except:
            await ctx.send("輸入錯誤，請重新輸入指令")

    @commands.command()
    async def choose(self, ctx, *args):
        chose = random.choice(args)
        response = [f"我覺得{chose}比較好!", f"{chose}看起來比較合理", f"絕對是{chose}了吧"]
        await ctx.send(random.choice(response))

    @commands.command()
    async def vote(self, ctx, *args):
        question = args[0]
        choices = args[1:]
        await ctx.message.delete()
        await ctx.send(f":bar_chart:{question}")
        embed = discord.Embed(colour=discord.Colour(0xF1C40F))
        emoji = {0: "1️⃣", 1: "2️⃣", 2: "3️⃣",
                 3: "4️⃣", 4: "5️⃣", 5: "6️⃣", 6: "7️⃣"}
        for i in range(len(choices)):
            embed.add_field(name=f"{emoji[i]}",
                            value=f"{choices[i]}", inline=True)
        msg = await ctx.send(embed=embed)
        for i in range(len(choices)):
            await msg.add_reaction(f"{emoji[i]}")

    @commands.command()
    async def coin(self, ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        while True:
            coins = ["正面", "反面"]
            result = random.choice(coins)
            await ctx.send("請輸入:正面 or 反面")
            try:
                response = await self.bot.wait_for("message", check=check)
                while response.content not in coins:
                    await ctx.send("輸入:正面 or 反面")
                    response = await self.bot.wait_for("message", check=check)
                guess = response.content
                if result == guess:
                    await ctx.send("猜對囉")
                elif result != guess:
                    await ctx.send("你猜錯了")
                time.sleep(1)
                await ctx.send("還要在玩一次嗎? (yes/no)")
                play_again = await self.bot.wait_for("message", check=check)
                if play_again.content.lower() != "yes":
                    await ctx.send("真的不玩了嗎!? 好吧")
                    break
            except:
                await ctx.send("輸入錯誤，請重新輸入指令")
                break

    @commands.command()
    async def daily(self, ctx, *goal):
        def check_emo(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        member = ctx.author
        data = ["小吉", "中吉", "大吉", "吉", "末吉", "凶", "大凶"]
        response = random.choices(data, weights=[40, 30, 5, 20, 50, 10, 5])
        answer, thing = "".join(response), "".join(goal)
        if not thing:
            await ctx.send(f"{member.mention} 【今日運氣預測】: ||{answer}||")
        else:
            for i in goal:
                response = random.choices(
                    data, weights=[40, 30, 5, 20, 50, 10, 5])
                answer = "".join(response)
                await ctx.send(f"{member.mention} 【{i}運氣預測】: ||{answer}||")

        if answer in ["凶", "大凶"]:
            await ctx.send("是否開啟轉運 (Y / N) :")
            response = await self.bot.wait_for("message", check=check)

            if response.content.lower() in ["yes", "y"]:
                embed = discord.Embed(
                    title="轉運時間", description=f"```現在是你的回合```")
                embed.add_field(
                    name="你有10秒做出選擇", value="", inline=False)
                msg = await ctx.send(embed=embed)
                embed = discord.Embed(colour=discord.Colour(0xF1C40F))
                emoji = {0: "1️⃣", 1: "2️⃣", 2: "3️⃣",
                        3: "4️⃣", 4: "5️⃣", 5: "6️⃣", 6: "7️⃣",
                        7: "8️⃣", 8: "9️⃣"}
                for i in range(9):
                    await msg.add_reaction(f"{emoji[i]}")
                try:
                    await ctx.bot.wait_for("reaction_add", timeout=10.0, check=check_emo)
                except asyncio.TimeoutError:
                    await ctx.send("時間結束! 你失去了")
                else:
                    await ctx.send("看來你做出了選擇")
                    result = random.choices(data, weights=[40, 30, 10, 20, 50, 5, 3])[0]
                    time.sleep(1)
                    await ctx.send(f"{member.mention} 轉運結果是: ||{result}||")
                    time.sleep(3)

                    if result == "凶":
                        await ctx.send("那我也沒辦法囉:man_shrugging:")
                    elif result == "大凶":
                        await ctx.send("那你最好還是別出門了:saluting_face:")
                    else:
                        await ctx.send("轉運成功的拉")

    @commands.command()
    async def rps(self, ctx):
        a = ["石頭", "剪刀", "布"]
        start = [
            ":crossed_swords: 來決鬥吧:crossed_swords: ",
            "區區一介凡人也妄想挑戰本喵:smirk: ",
            "就給你一個挑戰的機會吧:rolling_eyes: ",
        ]
        draw = ["本喵不過放水罷了:yawning_face: ",
                "竟然有和本喵相同的水準:face_with_raised_eyebrow: "]
        win = [
            "甚麼:interrobang: 竟然被打敗了",
            "不過僥倖被你贏了一次:triumph: ",
            "能夠贏過本喵，享受無上榮耀吧:unamused: ",
        ]
        lose = [
            "正常發揮罷了",
            "你想贏我先去練個800年吧",
            "失敗是對你的憐憫",
            ":place_of_worship: 膜拜本喵吧:place_of_worship: ",
        ]
        msg1 = None
        rules = {"石頭": "剪刀", "布": "石頭", "剪刀": "布"}

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        while True:
            answer = random.choice(a)
            await ctx.send(random.choice(start))
            time.sleep(1)
            await ctx.send("輸入:剪刀 or 石頭 or 布")
            time.sleep(1)
            msg1 = await self.bot.wait_for("message", check=check)
            while msg1.content not in a:
                await ctx.send("輸入:剪刀 or 石頭 or 布")
                time.sleep(1)
                msg1 = await self.bot.wait_for("message", check=check)
            msg = msg1.content
            await ctx.send("本喵出的是:" + answer)
            time.sleep(1)
            if msg == answer:
                await ctx.send("平手")
                time.sleep(1)
                await ctx.send(random.choice(draw))
            elif answer == rules[msg]:
                await ctx.send("你贏了")
                time.sleep(1)
                await ctx.send(random.choice(win))
            else:
                await ctx.send("你輸了")
                time.sleep(1)
                await ctx.send(random.choice(lose))
            time.sleep(1)
            await ctx.send("還要在玩一次嗎? (yes/no)")
            play_again = await self.bot.wait_for("message", check=check)
            if play_again.content.lower() != "yes":
                await ctx.send("真的不玩了嗎!? 好吧")
                break

    @commands.command()
    async def hangman(self, ctx):
        member = ctx.author
        word_list = jdata["單字"]
        word = random.choice(word_list)
        max_attempts = 6
        hangman_stages = [
            "```  +---+\n  |   |\n      |\n      |\n      |\n      |\n========```",
            "```  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n========```",
            "```  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n========```",
            "```  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n========```",
            "```  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n========```",
            "```  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n========```",
            "```  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========```"
        ]
        guessed_letters = ["_"] * len(word)
        incorrect_guesses = 0
        hidden_word = "_" * len(word)
        hangman_stage = 0
        hint = False

        message = await ctx.send(f"{member.mention} 遊戲開始")

        while incorrect_guesses < max_attempts and "_" in hidden_word:
            if hint:
                embed = discord.Embed(
                    title="提示開啟", description=f"```這下你總行了吧```")
                await message.edit(embed=embed)
                hint = False
                time.sleep(2)

            embed = discord.Embed(
                title="Hangman", description=f"```{hangman_stages[hangman_stage]}```")
            embed.add_field(
                name="單字", value=f"```{hidden_word}```", inline=False)
            embed.add_field(
                name="總字數", value=f"```{len(word)}個字母```", inline=False)
            embed.add_field(name="剩餘次數",
                            value=f"{incorrect_guesses}/{max_attempts}", inline=False)

            await message.edit(embed=embed)
            try:
                guess = await self.bot.wait_for("message", check=lambda msg: msg.author == ctx.author, timeout=60.0)
                guessed_letter = list(guess.content.lower())[:len(word)]
            except:
                embed = discord.Embed(
                    title="SO BAD", description=f"時間結束! YOU SUCH A FAILURE :melting_face: 單字是 {word}.")
                await message.edit(embed=embed)
                return False

            # Check if the guessed letter is in the word
            for idx, letter in enumerate(guessed_letter):
                if guessed_letters[idx] == "_":
                    if letter == word[idx]:
                        guessed_letters[idx] = letter
            else:
                incorrect_guesses += 1
                hangman_stage += 1

            hidden_word = "".join(guessed_letters)

            if len(word) > 4 and max_attempts - incorrect_guesses <= 2 and hidden_word.count("_") >= len(hidden_word) - 1:
                hint = True
                for i in random.sample([i for i in range(0, len(word))], 3 if len(word) <= 7 else len(word) - 4):
                    guessed_letters[i] = word[i]
                    hidden_word = "".join(guessed_letters)

        # Create the final embed with the result of the game
        embed = discord.Embed(title="Hangman")
        if "_" not in hidden_word:
            embed.description = f"おめでとう, 你猜中了 {word}!"
            embed.add_field(
                name="單字", value=f"```{word}```", inline=False)
            embed.color = discord.Color.green()
            await ctx.send(embed=embed)
            return True
        else:
            embed.description = f"再多時間都不夠你用 Haiya :yawning_face: 單字是 {word}."
            embed.color = discord.Color.red()
            await ctx.send(embed=embed)
            return False

    @commands.command()
    async def roll(self, ctx, number):
        member = ctx.author
        try:
            num = random.randint(1, number)
            await ctx.send(f"{member.mention} 結果是 {num}")
        except ValueError:
            await ctx.send("請輸入數字")


async def setup(bot):
    await bot.add_cog(Game(bot))
