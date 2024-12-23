import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import json
from config import guild_id

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_roles(self):
        guild = self.bot.get_guild(guild_id)
        roles = [role.name for role in guild.roles]
        print(roles)
        return roles

    @app_commands.command(name='addinfofield', description="Create a new role")
    @app_commands.guilds(guild_id)
    async def addinfofield(self, interaction: discord.Interaction, field: str):
        with open('members.json', 'r') as rf:
            members = json.load(rf)
        
        for member in members:
            member[field] = 

        field.title()




    # @app_commands.command(name='createrole', description="Create a new role")
    # @app_commands.guilds(guild_id)
    # async def createrole(self, interaction: discord.Interaction, role_name: str, role_hex_color: str, ):
    #     guild = interaction.guild
        
    #     #discord.Permissions.
    #     try:
    #         color = discord.Color.from_str(role_hex_color)
    #     except ValueError:
    #         await interaction.response.send_message(f"The color f'{role_hex_color}' is not valid. Use the #FFFFFF format")
        

    #     self.get_roles()



async def setup(bot):
    await bot.add_cog(Admin(bot))