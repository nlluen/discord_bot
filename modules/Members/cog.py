import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import json
import pytz
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
    
    @app_commands.command(name='register', description='Register your information')
    @app_commands.guilds(guild_id)
    async def register(self, interaction: discord.Interaction, name: str, birthday: str):
        member_name = name.title().strip()
        member_id = interaction.user.id
        member_join_date = interaction.user.joined_at.astimezone(pytz.timezone('US/Eastern')).strftime('%m/%d/%Y at %H:%M:%S')

        try:
            birthday_date = datetime.strptime(birthday, '%m/%d')            
            formatted_birthday = f'{birthday_date.month}/{birthday_date.day}'
            
        except ValueError:
            await interaction.response.send_message("Please input a valid calendar date in the mm/dd format", ephemeral=True)
            return
        
        dic = {
            "Name": member_name,
            "Birthday": formatted_birthday,
             # "Member_ID": member_id,
            "Join_Date": member_join_date,
            "Dabloons": 0
        }

        print(dic)  
        members = self.get_registered_members()
        if str(member_id) in members:
            await interaction.response.send_message(f'<@{member_id}> You have already register!', ephemeral=True)
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
            await interaction.response.send_message(f'<@{member_id}> You have successfully unregistered.',  ephemeral=True)
            self.update_registered_members(members)
        else:
            await interaction.response.send_message(f'<@{member_id}> Try registering first with /register !', ephemeral=True)
    
    @app_commands.command(name='info', description='Display your registed information')
    @app_commands.guilds(guild_id)
    async def info(self, interaction: discord.Interaction, user: discord.User = None):
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
            pfp = member.display_avatar
            em = discord.Embed(title=f"{member.display_name}'s Information", color=discord.Color.blue())
            em.add_field(name='Name', value=name, inline=True)
            em.add_field(name='Birthday', value=birthday, inline=True)
            em.add_field(name='Dabloons', value=dabloons, inline=False)
            em.add_field(name='Server Join Date', value=join_date, inline=False)
            em.set_thumbnail(url=f'{pfp}')
            await interaction.response.send_message(embed=em)
    
    @app_commands.command(name='av', description="Display your own or someone else's profile picture")
    @app_commands.guilds(guild_id)
    async def av(self, interaction: discord.Interaction, user: discord.User = None):
        if user is None:
            member = interaction.user
        else:
            member = user
        
        pfp = member.display_avatar
        em = discord.Embed(title=f"{member.display_name}'s Avatar", color=discord.Color.blue())
        em.set_image(url=member.display_avatar)
        await interaction.response.send_message(embed=em)

            
async def setup(bot):
    await bot.add_cog(Member(bot))