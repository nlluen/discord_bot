import discord
from discord.ext import commands
from discord import app_commands
from config import guild_id
import random




    
class Fish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # async def cog_load(self):
    #     print('hello')
    #     self.bot.tree.add_command(FishGroup(self.bot))

    #@app_commands.command(name="delete_announcement", description="Delete any announcement by index")
    #@app_commands.guilds(guild_id)
    # @app_commands.commands(name="fish", description="Spawn a Fish", guild_ids=[guild_id])
    # async def fish(self, interaction: discord.Interaction):
    #     interaction.response.send_message("h", ephemeral=True)
    #     spawn = random.randint(1, 50)

    #     # if 

    # # @fish_group.command(name="fish", description="Spawn a fish")
    # # async def fish(interaction: discord.Interaction):
    # #     await interaction.response.send_message("Hi", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Fish(bot))