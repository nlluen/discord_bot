import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta
import json
from config import guild_id, announcement_channel_id, mod_role_id, godmother_role_id, admin_role_id

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_roles(self):
        guild = self.bot.get_guild(guild_id)
        roles = [role.name for role in guild.roles]
        print(roles)
        return roles


    @app_commands.command(name='give_role', description="Give a user a role")
    @app_commands.guilds(guild_id)
    @app_commands.checks.has_any_role(admin_role_id, godmother_role_id, mod_role_id)
    async def give_role(self, interaction: discord.Interaction, user: discord.Member, role: discord.Role):
        user_roles = user.roles
        restricted_roles = ["Men", "Untitled", "Champion of Halloween",
                            "The Godfather", "The Godmother", "The Godson", "ECE"]

        if role.name in restricted_roles:
            await interaction.response.send_message("This is a restricted role.", ephemeral=True)

        if role not in user_roles:
            await user.add_roles(role)
            await interaction.response.send_message(f"You have given {user.display_name} the {role.name} Role.", ephemeral=True)
        else:
            await interaction.response.send_message(f"{user.display_name} already has this role.")

    @app_commands.command(name='take_role', description="Take away a user's role")
    @app_commands.guilds(guild_id)
    @app_commands.checks.has_any_role(admin_role_id, godmother_role_id, mod_role_id)
    async def take_role(self, interaction: discord.Interaction, user: discord.Member, role: discord.Role):
        user_roles = user.roles

        if role in user_roles:
            await user.remove_roles(role)
            await interaction.response.send_message(f"Removed {role.name} Role from {user.display_name}.", ephemeral=True)
        else:
            await interaction.response.send_message(f"{user.display_name} does not have this role.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Admin(bot))