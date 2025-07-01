import discord
from discord.ext import commands
from discord import app_commands
from config import guild_id, announcement_channel_id
import asyncio
import random
import pytz
import json


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.has_any_role('Untitled', 'The Godfather')
    @commands.command(name='purge', help='purge x amount of message')
    async def purge(self, ctx, arg: int):
        if arg <= 25:
            await ctx.channel.purge(limit=arg + 1)
            await asyncio.sleep(3)

    @app_commands.command(name='poll', description='create a poll with up to 10 inputs', )
    @app_commands.guilds(guild_id)
    async def poll(self, interaction: discord.Interaction, title: str, option1: str, option2: str, option3: str = None,
                   option4: str = None, option5: str = None, option6: str = None, option7: str = None,
                   option8: str = None, option9: str = None, option10: str = None):
        number_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
        options = [option1, option2, option3, option4, option5, option6, option7, option8, option9, option10]
        valid_options = [option for option in options if option is not None]
        embed = discord.Embed(title=title, color=discord.Color.dark_gold())

        for i, option in enumerate(valid_options):
            embed.add_field(name=f'{i + 1}) {option}', value='', inline=False)

        await interaction.response.send_message(embed=embed)

        original_response = await interaction.original_response()

        for i in range(len(valid_options)):
            await original_response.add_reaction(number_emojis[i])

    @app_commands.command(name='flip', description='Flip a coin to make your basic life choices')
    @app_commands.guilds(guild_id)
    async def flip(self, interaction: discord.Interaction, guess: str = None):
        HoT = random.randint(0, 1)

        if guess is not None:
            guess = guess.lower()
            if HoT:
                side = 'Heads'
            else:
                side = 'Tails'

            if guess == side.lower():
                await interaction.response.send_message(f"You were correct! It was {side}")
            else:
                await interaction.response.send_message(f"You were wrong! It was {side}")
            return

        if HoT:
            await interaction.response.send_message("Heads!")
        else:
            await interaction.response.send_message("Tails!")

    @app_commands.command(name='add_role', description='Give yourself a role')
    @app_commands.guilds(guild_id)
    async def add_role(self, interaction: discord.Interaction, role: discord.Role):
        roles = interaction.user.roles
        restricted_roles = ["Men", "Untitled", "Champion of Halloween", "The Godfather", "The Godmother", "The Godson",
                            "ECE", "Hall Of Shame"]
        if role not in roles and role.name not in restricted_roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"You have been given the *{role}* role", ephemeral=True)
        elif role in roles:
            await interaction.response.send_message("You already have this role!", ephemeral=True)
        else:
            await interaction.response.send_message("Sorry but you cannot access that role!", ephemeral=True)

    @app_commands.command(name='remove_role', description='Remove a role')
    @app_commands.guilds(guild_id)
    async def remove_role(self, interaction: discord.Interaction, role: discord.Role):
        roles = interaction.user.roles
        if role in roles:
            await interaction.user.remove_roles(role)
            await interaction.response.send_message(f"Successfully removed the {role} role!", ephemeral=True)
        else:
            await interaction.response.send_message("You cannot remove a role you do not have!", ephemeral=True)

    @app_commands.command(name="roleinfo", description="Get the information about a role")
    @app_commands.guilds(guild_id)
    async def role_info(self, interaction: discord.Interaction, role: discord.Role):
        members_with_role = [member for member in role.members]
        member_names = " • ".join([member.display_name for member in members_with_role])

        embed = discord.Embed(title=f"Role Info: {role.name}", color=discord.Color.blue())
        embed.add_field(name="Members with this role", value=len(members_with_role), inline=False)
        embed.add_field(name="Members", value=member_names, inline=False)
        embed.add_field(name="Role ID", value=role.id, inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name='serverinfo', description='Get the general info for the server!')
    @app_commands.guilds(guild_id)
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        guild_name = guild.name
        guild_description = guild.description
        guild_icon_url = guild.icon.url
        guild_creation_date = guild.created_at.strftime("%m/%d/%Y at %I:%M %p")
        guild_member_count = guild.member_count
        guild_channels = await guild.fetch_channels()
        guild_text_channel_count = sum(1 for channel in guild_channels if isinstance(channel, discord.TextChannel))
        guild_voice_channel_count = sum(1 for channel in guild_channels if isinstance(channel, discord.VoiceChannel))
        embed = discord.Embed(title=guild_name, color=discord.Color.dark_gold())
        embed.description = guild_description
        embed.set_thumbnail(url=guild_icon_url)
        embed.add_field(name="Created on", value=guild_creation_date)
        embed.add_field(name="Members", value=guild_member_count)
        embed.add_field(name="Text Channels", value=guild_text_channel_count, inline=False)
        embed.add_field(name="Voice Channels", value=guild_voice_channel_count)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="servericon", description="Get the server's current icon!")
    @app_commands.guilds(guild_id)
    async def servericon(self, interaction: discord.Interaction):
        guild = interaction.guild
        guild_icon_url = guild.icon.url
        guild_name = guild.name
        embed = discord.Embed(title=f"{guild_name}'s Icon", color=discord.Color.dark_gold())
        embed.set_image(url=guild_icon_url)
        await interaction.response.send_message(embed=embed)

    # @app_commands.command(name="create_announcement", description="Queue your announcement for a mod to approve")
    # @app_commands.guilds(guild_id)
    # async def create_announcement(self, interaction: discord.Interaction, brief_description: str, message: str):
    #
    #     # print(interaction.created_at.astimezone(pytz.timezone('US/Eastern')).strftime('%m/%d/%Y at %H:%M:%S'))
    #     dic = {
    #         "Description": brief_description,
    #         "Message": message,
    #         "Announcer": interaction.user.id,
    #         "Time_Created": interaction.created_at.astimezone(pytz.timezone('US/Eastern')).strftime(
    #             '%m/%d/%Y at %I:%M %p')
    #     }
    #
    #     with open('announcements.json', 'r') as rf:
    #         announcements = json.load(rf)
    #
    #     if len(announcements) == 5:
    #         await interaction.response.send_message("Too many announcements queued, ask the mods to clear them.")
    #         return
    #
    #     announcements.append(dic)
    #
    #     with open('announcements.json', 'w') as wf:
    #         json.dump(announcements, wf, indent=4)
    #
    #     await interaction.response.send_message(
    #         "Thank you for your announcement, a mod will review and approve it shortly.")
    #
    # @app_commands.command(name='announcements', description="View all queued announcements")
    # @app_commands.guilds(guild_id)
    # async def announcements(self, interaction: discord.Interaction):
    #     embed = discord.Embed(title="Announcements Queued", color=discord.Color.blue())
    #
    #     with open("announcements.json", 'r') as rf:
    #         announcements = json.load(rf)
    #
    #     embed.description = ""
    #     for i, announcement in enumerate(announcements):
    #         # print(announcement)
    #         announcer = interaction.guild.get_member(announcement['Announcer'])
    #         embed.description += f"{i + 1}: " + f"{announcement['Description']} - {announcer.display_name}" + "\n"
    #         # embed.add_field(name= f"{i+1}", value= f"{announcement['Description']}", inline=True)
    #         # embed.add_field(name="Time Queued", value=f"{announcement['Time_Created']}", inline=True)
    #
    #     await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Utility(bot))