# import discord
# from discord.ext import commands
# from discord import app_commands
# from datetime import datetime, timedelta
# import json
# from config import guild_id, announcement_channel_id, mod_role_id, godmother_role_id, admin_role_id
#
#
# # class ConfirmView(discord.ui.View):
#
# #     # Confirmation button
# #     @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
# #     async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
# #         await interaction.response.send_message("You confirmed! Proceeding...", ephemeral=True)
#
# #     # Decline button
# #     @discord.ui.button(label="No", style=discord.ButtonStyle.red)
# #     async def decline_button(self, interaction: discord.Interaction, button: discord.ui.Button):
# #         await interaction.response.send_message("You declined. Cancelling...", ephemeral=True)
#
#
# class Admin(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#
#     def get_roles(self):
#         guild = self.bot.get_guild(guild_id)
#         roles = [role.name for role in guild.roles]
#         print(roles)
#         return roles
#
#     # @app_commands.command(name='addinfofield', description="Create a new role")
#     # @app_commands.guilds(guild_id)
#     # @app_commands.check(is_mod)
#     # async def addinfofield(self, interaction: discord.Interaction, field: str):
#     #     with open('members.json', 'r') as rf:
#     #         members = json.load(rf)
#
#     #     for member in members:
#     #         member[field] =
#
#     #     field.title()
#     #     return
#
#     @app_commands.command(name='give_role', description="Give a user a role")
#     @app_commands.guilds(guild_id)
#     @app_commands.checks.has_any_role(admin_role_id, godmother_role_id, mod_role_id)
#     async def give_role(self, interaction: discord.Interaction, user: discord.Member, role: discord.Role):
#         user_roles = user.roles
#         restricted_roles = ["Men", "Untitled", "Champion of Halloween",
#                             "The Godfather", "The Godmother", "The Godson", "ECE"]
#
#         if role.name in restricted_roles:
#             await interaction.response.send_message("This is a restricted role.", ephemeral=True)
#
#         if role not in user_roles:
#             await user.add_roles(role)
#             await interaction.response.send_message(f"You have given {user.display_name} the {role.name} Role.", ephemeral=True)
#         else:
#             await interaction.response.send_message(f"{user.display_name} already has this role.")
#
#     @app_commands.command(name='take_role', description="Take away a user's role")
#     @app_commands.guilds(guild_id)
#     @app_commands.checks.has_any_role(admin_role_id, godmother_role_id, mod_role_id)
#     async def take_role(self, interaction: discord.Interaction, user: discord.Member, role: discord.Role):
#         user_roles = user.roles
#
#         if role in user_roles:
#             await user.remove_roles(role)
#             await interaction.response.send_message(f"Removed {role.name} Role from {user.display_name}.", ephemeral=True)
#         else:
#             await interaction.response.send_message(f"{user.display_name} does not have this role.", ephemeral=True)
#
#
#
#
#
#     # @app_commands.command(name='reset_emotes', description="Take away a user's role")
#     # @app_commands.guilds(guild_id)
#     # @app_commands.check(is_mod)
#     # async def reset_emotes(self, interaction: discord.Interaction):
#     #     await interaction.response.send_message("Are you sure you want to reset all emotes to the default?", view=)
#
#     # @app_commands.command(name='approve_announcement', description="Approve the announcement of your choosing")
#     # @app_commands.guilds(guild_id)
#     # @app_commands.check(is_mod)
#     # async def approve_announcement(self, interaction: discord.Interaction, index: int):
#
#     #     index -= 1
#
#     #     with open("announcements.json", 'r') as rf:
#     #         announcements = json.load(rf)
#
#     #     if len(announcements) == 0:
#     #         await interaction.response.send_message("No announcements to approve!", ephemeral=True)
#     #         return
#
#     #     if 0 >= index or index >= len(announcements):
#     #         await interaction.response.send_message("Index invalid", ephemeral=True)
#     #         return
#
#     #     announcement = announcements[index]
#     #     announcer = interaction.guild.get_member(announcement['Announcer'])
#     #     pfp = announcer.display_avatar
#     #     embed = discord.Embed(
#     #         title=f"{announcer.display_name}'s Announcement", color=discord.Color.blue())
#     #     embed.description = announcement['Message']
#     #     embed.set_thumbnail(url=pfp)
#
#     #     await interaction.response.send_message("The announcement is now posted!", ephemeral=True)
#     #     await self.bot.get_channel(announcement_channel_id).send(embed=embed)
#
#     #     announcements.pop(index)
#
#     #     with open('announcements.json', 'w') as wf:
#     #         json.dump(announcements, wf, indent=4)
#
#     # @app_commands.command(name="delete_announcement", description="Delete any announcement by index")
#     # @app_commands.guilds(guild_id)
#     # @app_commands.check(is_mod)
#     # async def delete_announcement(self, interaction: discord.Interaction, index: int):
#     #     with open("announcements.json", 'r') as rf:
#     #         announcements = json.load(rf)
#
#     #     if len(announcements) == 0:
#     #         await interaction.response.send_message("Index invalid")
#     #         return
#
#     #     if 0 >= index or index >= len(announcements):
#     #         await interaction.response.send_message("Index invalid")
#     #         return
#
#     #     announcements.pop(index)
#
#     #     await interaction.response.send_message("Successfully deleted announcement")
#
#     # @app_commands.command(name='create_emote', description="Create a new emote")
#     # @app_commands.guilds(guild_id)
#     # @app_commands.check(is_mod)
#     # async def create_emote(self, interaction: discord.Interaction, image: discord.Attachment):
#     #     guild = interaction.guild
#     #     print(len(guild.emojis))
#     #     if ((guild.premium_tier == 0 and len(guild.emojis) == 50) or
#     #         (guild.premium_tier == 1 and len(guild.emojis) == 100) or
#     #         (guild.premium_tier == 2 and len(guild.emojis) == 150) or
#     #             (guild.premium_tier == 3 and len(guild.emojis) == 250)):
#     #         print(len(guild.emojis))
#     #         await interaction.response.send_message(
#     #             "The list of emotes is full!", ephemeral=True)
#
#     #     image.
#     #     await guild.create_custom_emoji
#
#     # @app_commands.command(name='timeout', description="Timeout a member.")
#     # @app_commands.guilds(guild_id)
#     # @app_commands.check(is_mod)
#     # async def timeout(self, interaction: discord.Interaction, user: discord.Member, days: int, reason: str = None):
#     #     duration = timedelta(days=days)
#     #     user.timeout(duration = duration, reason=reason)
#
#     # @app_commands.command(name='createrole', description="Create a new role")
#     # @app_commands.guilds(guild_id)
#     # async def createrole(self, interaction: discord.Interaction, role_name: str, role_hex_color: str, ):
#     #     guild = interaction.guild
#
#     #     #discord.Permissions.
#     #     try:
#     #         color = discord.Color.from_str(role_hex_color)
#     #     except ValueError:
#     #         await interaction.response.send_message(f"The color f'{role_hex_color}' is not valid. Use the #FFFFFF format")
#
#     #     self.get_roles()
#
#
# async def setup(bot):
#     await bot.add_cog(Admin(bot))
