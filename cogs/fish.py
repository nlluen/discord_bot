import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta
import json
from config import guild_id, announcement_channel_id, mod_role_id, godmother_role_id, admin_role_id

@app_commands.guilds(guild_id)
class Fish(commands.GroupCog, name='fish', group_name='fish', group_description='Fishing commands!'):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name='spawn', description='Spawn a fish.')
    #@app_commands.guilds(guild_id)
    async def spawn(self, interaction: discord.Interaction):
        await interaction.response.send_message("Fish has spawned")

    @app_commands.command(name='catch', description='Catch a fish.')
    # @app_commands.guilds(guild_id)
    async def catch(self, interaction: discord.Interaction):
        await interaction.response.send_message("Fish has been caught!")

async def setup(bot) -> None:
    await bot.add_cog(Fish(bot))