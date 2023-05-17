import discord
from discord.ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(colour=discord.Colour(
            0xf1c40f), url="https://discordapp.com", description="這是Matcha News的指令協助")
        embed.set_thumbnail(url="https://i.imgur.com/ql63KCT.jpg")
        embed.set_author(name="Matcha News")
        embed.add_field(
            name="1. Ping", value="查看延遲\n用法: `-ping`", inline=False)
        embed.add_field(name="2. Cat", value="貓貓圖片\n用法: `-cat`", inline=False)
        embed.add_field(
            name="3. Say", value="讓機器人學你說話\n用法: `-say`", inline=False)
        embed.add_field(name="4. Clear",
                        value="清除頻道訊息\n用法: `-clear [訊息數量]`", inline=False)
        embed.add_field(
            name="5. Load", value="導入類別\n用法: `-load [類別]`", inline=False)
        embed.add_field(name="6. Reload",
                        value="重新導入類別\n用法: `-reload [類別]`", inline=False)
        embed.add_field(name="7. Unload",
                        value="導出類別\n用法: `-unload [類別]`", inline=False)
        embed.add_field(name="8. Rock Peper Scissor",
                        value="和機器人用剪刀石頭布一決勝負\n用法: `-rps`", inline=False)
        embed.add_field(name="9. Guess Number",
                        value="猜數字遊戲\n用法: `-gn`", inline=False)
        embed.add_field(name="10. Choose",
                        value="讓機器人幫你選擇\n用法: `-choose [選擇]`", inline=False)
        embed.add_field(name="11. Coin",
                        value="擲硬幣\n用法: `-coin`", inline=False)
        embed.add_field(name="12. Daily",
                        value="預測今日運氣\n用法: `-daily`", inline=False)
        embed.add_field(
            name="13. Vote", value="投票系統\n用法: `-vote [題目] [後續選項依序用空格分隔(至多七項)]`", inline=False)
        embed.add_field(name="14. meal",
                        value="選餐系統\n用法: `-meal`", inline=False)
        embed.add_field(name="15. hangman",
                        value="猜字遊戲\n用法: `-hangman`", inline=False)
        embed.add_field(name="16. roll",
                        value="隨機取數\n用法: `-roll [數字]`", inline=False)
        embed.add_field(name="17. 1A2B",
                        value="1A2B玩起來\n用法: `-password [位數]`", inline=False)
        embed.add_field(name="18. Help",
                        value="顯示此視窗\n用法: `-help`", inline=False)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Main(bot))
