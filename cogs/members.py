import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import json
import pytz
import re
from config import guild_id


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_registered_members(self):
        with open('members.json', 'r') as rf:
            members = json.load(rf)
        return members

    def update_registered_members(self, members):
        with open('members.json', 'w') as file:
            json.dump(members, file, indent=4)

    @app_commands.command(name='register_color', description='Add or update your server color')
    @app_commands.guilds(guild_id)
    async def register_color(self, interaction: discord.Interaction, color: str):
        members = self.get_registered_members()
        color_str_pattern1 = r"^[0-9A-Fa-f]{6}$"
        color_str_pattern2 = r"^#[0-9A-Fa-f]{6}$"
        user_id_str = str(interaction.user.id)

        if re.match(color_str_pattern1, color):
            color = f"#{color}"

        if not re.match(color_str_pattern2, color):
            await interaction.response.send_message("Please input the hexcode for your color in #000000 format",
                                                    ephemeral=True)
            return

        if user_id_str in members:
            members[user_id_str]["Color"] = color
            self.update_registered_members(members)
            await interaction.response.send_message("Your Color has been added!", ephemeral=True)

    @app_commands.command(name='register', description='Register your information')
    @app_commands.guilds(guild_id)
    async def register(self, interaction: discord.Interaction, name: str, birthday: str, color: str = None):
        member_name = name.title().strip()
        member_id = interaction.user.id
        member_join_date = interaction.user.joined_at.astimezone(pytz.timezone('US/Eastern')).strftime(
            '%m/%d/%Y at %I:%M:%S %p')

        if color is None:
            color = "#000000"
        else:
            color_str_pattern = r"^[0-9A-Fa-f]{6}$"

            if re.match(color_str_pattern, color):
                color = f"#{color}"

            color_str_pattern2 = r"^#[0-9A-Fa-f]{6}$"
            if not re.match(color_str_pattern2, color):
                await interaction.response.send_message("Please input the hexcode for your color in #000000 format",
                                                        ephemeral=True)
                return

        try:
            birthday_date = datetime.strptime(birthday, '%m/%d')
            formatted_birthday = f'{birthday_date.month}/{birthday_date.day}'

        except ValueError:
            await interaction.response.send_message("Please input a valid calendar date in the mm/dd format",
                                                    ephemeral=True)
            return

        dic = {
            "Name": member_name,
            "Birthday": formatted_birthday,
            # "Member_ID": member_id,
            "Join_Date": member_join_date,
            "Dabloons": 0,
            "Color": color
        }

        print(dic)
        members = self.get_registered_members()
        if str(member_id) in members:
            await interaction.response.send_message(f'<@{member_id}> You have already registered!', ephemeral=True)
        else:
            await interaction.response.send_message(f'<@{member_id}> Thank you for registering!', ephemeral=True)
            members[member_id] = dic
            self.update_registered_members(members)

    @app_commands.command(name='unregister', description='Unregister your information')
    @app_commands.guilds(guild_id)
    async def unregister(self, interaction: discord.Interaction):
        members = self.get_registered_members()
        member_id = str(interaction.user.id)
        if member_id in members:
            del members[member_id]
            await interaction.response.send_message(f'<@{member_id}> You have successfully unregistered.',
                                                    ephemeral=True)
            self.update_registered_members(members)
        else:
            await interaction.response.send_message(f'<@{member_id}> Try registering first with /register !',
                                                    ephemeral=True)

    @app_commands.command(name='info', description='Display your registered information')
    @app_commands.guilds(guild_id)
    async def info(self, interaction: discord.Interaction, user: discord.Member = None):
        if user is None:
            member_id = str(interaction.user.id)
            member = interaction.user
        else:
            member_id = str(user.id)
            member = user

        members = self.get_registered_members()
        if member_id in members:
            name = members[member_id]["Name"]
            birthday = members[member_id]["Birthday"]
            dabloons = members[member_id]["Dabloons"]
            join_date = members[member_id]["Join_Date"]
            color = members[member_id]["Color"]
            pfp = member.display_avatar
            roles = member.roles
            role_str = " • ".join([role.name for role in roles])
            em = discord.Embed(title=f"{member.display_name}'s Information", color=discord.Color.from_str(color))
            em.add_field(name='Name', value=name)
            em.add_field(name='Birthday', value=birthday)
            em.add_field(name='Dabloons', value=dabloons, inline=False)
            em.add_field(name='Color', value=color)
            em.add_field(name='Server Join Date', value=join_date, inline=False)
            em.add_field(name="Roles", value=role_str)
            em.set_thumbnail(url=f'{pfp}')
            await interaction.response.send_message(embed=em)
        else:
            await interaction.response.send_message("Try registering first!", ephemeral=True)

    @app_commands.command(name='av', description="Display your own or someone else's profile picture")
    @app_commands.guilds(guild_id)
    async def av(self, interaction: discord.Interaction, user: discord.User = None):
        if user is None:
            member = interaction.user
        else:
            member = user

        pfp = member.display_avatar

        member_id = str(member.id)
        members = self.get_registered_members()

        if member_id in members:
            color = discord.Color.from_str(members[member_id]["Color"])
        else:
            color = discord.Color.blue()

        em = discord.Embed(title=f"{member.display_name}'s Avatar", color=color)
        em.set_image(url=pfp)
        await interaction.response.send_message(embed=em)

    @app_commands.command(name="birthday", description="Display all or a specific registered birthday(s) in the server")
    @app_commands.guilds(guild_id)
    async def birthday(self, interaction: discord.Interaction, user: discord.User = None):
        members = self.get_registered_members()

        if user is None:
            date_format = "%m/%d"

            sorted_birthdays = dict(
                sorted(
                    members.items(),
                    key=lambda x: (datetime.strptime(x[1]["Birthday"], date_format), x[1]["Name"])
                )
            )

            embed = discord.Embed(title=f"Degen Birthdays - {len(sorted_birthdays)}", color=discord.Color.blue())
            for member_id, member_data in sorted_birthdays.items():
                name = member_data["Name"]
                birthday = member_data["Birthday"]
                embed.add_field(name=name, value=birthday, inline=False)
            await interaction.response.send_message(embed=embed)

        else:
            user_id = str(user.id)
            if user_id in members:
                birthday = members[user_id]["Birthday"]
                color = members[user_id]["Color"]
                pfp = user.display_avatar
                embed = discord.Embed(title=f"{user.display_name}'s Birthday", color=discord.Color.from_str(color))
                embed.description = f"{birthday}"
                embed.set_thumbnail(url=pfp)
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("This user has not registered!", ephemeral=True)
                return


async def setup(bot):
    await bot.add_cog(Member(bot))