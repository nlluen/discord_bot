import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timedelta
from typing import Optional
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
    async def give_role(
            self, interaction: discord.Interaction,
            role: discord.Role,
            user1: discord.Member,
            user2: Optional[discord.Member],
            user3: Optional[discord.Member],
            user4: Optional[discord.Member],
            user5: Optional[discord.Member],
            user6: Optional[discord.Member],
            user7: Optional[discord.Member],
            user8: Optional[discord.Member],
            user9: Optional[discord.Member],
            user10: Optional[discord.Member]
    ):

        restricted_roles = ["Men", "Untitled", "Champion of Halloween",
                            "The Godfather", "The Godmother", "The Godson", "ECE"]

        if role.name in restricted_roles:
            await interaction.response.send_message("This is a restricted role.", ephemeral=True)

        members = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]

        members_given_role = []
        roel_not_given = []

        for member in members:
            if member is not None:
                member_roles = member.roles
                if role not in member_roles:
                    await member.add_roles(role)
                    members_given_role.append(member)
                    #await interaction.response.send_message(f"You have given {member.display_name} the {role.name} Role.", ephemeral=True)

        if members_given_role:
            names = ', '.join(member.display_name for member in members_given_role)
            await interaction.response.send_message(f" '{names}' have been given the {role.name} Role")



    @app_commands.command(name='take_role', description="Take away a user's role")
    @app_commands.guilds(guild_id)
    @app_commands.checks.has_any_role(admin_role_id, godmother_role_id, mod_role_id)
    async def take_role(
            self,
            interaction: discord.Interaction,
            role: discord.Role,
            user1: discord.Member,
            user2: Optional[discord.Member],
            user3: Optional[discord.Member],
            user4: Optional[discord.Member],
            user5: Optional[discord.Member],
            user6: Optional[discord.Member],
            user7: Optional[discord.Member],
            user8: Optional[discord.Member],
            user9: Optional[discord.Member],
            user10: Optional[discord.Member]
    ):

        members = [user1, user2, user3, user4, user5, user6, user7, user8, user9, user10]
        members_remove_roles = []

        for member in members:
            if member is not None:
                member_roles = member.roles
                if role in member_roles:
                    await member.remove_roles(role)
                    members_remove_roles.append(member)
                    #await interaction.response.send_message(f"You have given {member.display_name} the {role.name} Role.", ephemeral=True)




        if members_remove_roles:
            names = ', '.join(member.display_name for member in members_remove_roles)
            await interaction.response.send_message(f"Removed '{names}' Role from the {role.name} Role")

        # if role in user_roles:
        #     await user.remove_roles(role)
        #     await interaction.response.send_message(f"Removed {role.name} Role from {user.display_name}.", ephemeral=True)
        # else:
        #     await interaction.response.send_message(f"{user.display_name} does not have this role.", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Admin(bot))