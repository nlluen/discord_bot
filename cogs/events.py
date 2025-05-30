import discord
from discord.ext import commands
from discord import app_commands
from config import guild_id, announcement_channel_id, welcome_channel_id


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        welcome_channel = self.bot.get_channel(welcome_channel_id)
        if welcome_channel:
            await welcome_channel.send(f"Welcome to the Degenerates of RU'23, {member.mention}. Have fun, be nice, and be a degenerate")

    # @commands.Cog.listener()
    # async def on_member_leave(self, member: discord.Member):

    # @commands.Cog.listener()
    # async def


async def setup(bot):
    await bot.add_cog(Events(bot))