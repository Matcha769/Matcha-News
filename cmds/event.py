import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json

# open json file to read channel id
with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    # Bot info set up
    @commands.Cog.listener()
    async def on_ready():
        activity = discord.Game(name="勥烎菿奣", type=3)
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        print(">> Bot is online <<")

    # react when "詩音" in message
    @commands.Cog.listener()
    async def on_message(message):
        await bot.process_commands(message)
        i, ma, se = "\u3044", "\u307e", "\u305b"
        if "詩音" in message.content and not (message.author.bot):
            channel = message.channel
            member = message.author
            await channel.send(f'{member.mention} {i}{ma}幸{se}?')

    # send message when people join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata['日常聊天']))
        await channel.send(f'{member} join!')

    # send message when people leave
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata['日常聊天']))
        await channel.send(f'{member} leave!')

def setup(bot):
    bot.add_cog(Event(bot))
