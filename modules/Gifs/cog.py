from discord.ext import commands
ignore_message_delete = False
import time
import random

class Gifs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_ignore_message(self) -> bool:
        global ignore_message_delete
        return ignore_message_delete

    def set_ignore_message(self, ignore_message: bool):
        global ignore_message_delete
        ignore_message_delete = ignore_message

    @commands.command(name='squidward', help='Sends the squidward glass shatter gif')
    async def squidward(self, ctx):
        self.set_ignore_message(True)
        try:
            await ctx.message.delete()
            await ctx.send('https://tenor.com/view/squidward-tonight-glass-break-kinemaster-gif-22142436')
        finally:
            self.set_ignore_message(False)

    @commands.command(name='nerd', help='Sends a nerd gif')
    async def nerd(self, ctx):
        self.set_ignore_message(True)
        try:
            await ctx.message.delete()
            await ctx.send('https://tenor.com/view/nerd-emoji-nerd-emoji-avalon-play-avalon-gif-24241051')
        finally:
            self.set_ignore_message(False)

    @commands.command(name='grind', help='the grind starts')
    async def grind(self, ctx):
        self.set_ignore_message(True)
        try:
            await ctx.message.delete()
            await ctx.send('https://cdn.discordapp.com/attachments/752401958647890108/1079994924906324089/Screenshot_20220713-163149_YouTube.jpg')
        finally:
            self.set_ignore_message(False)

    @commands.command(name='capcheck', help='checks for cap')
    async def capcheck(self, ctx):
        await ctx.send('https://tenor.com/view/cap-cap-check-gif-24989004')
        await ctx.send("CAP CHECK RESULTS:")
        time.sleep(3.0)
        HoT = random.randint(0, 1)
        if HoT:
            await ctx.send('cap')
        else:
            await ctx.send('not cap')


async def setup(bot):
    await bot.add_cog(Gifs(bot))