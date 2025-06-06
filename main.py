import discord
from discord import app_commands
from discord.ext import commands
from discord import Interaction
import asyncio
import os
from config import guild_id, bot_test_channel_id
from dotenv import load_dotenv

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='+', intents=intents)

#print(os.getenv('TOKEN'))

# class FishGroup(app_commands.Group):

#     def __init__(self):
#         super().__init__(name="fish", description="Fish group")
#         # self.bot = bot

#     #@app_commands.guilds(guild_id)
#     @app_commands.command(name="catch", description="catch the fish!")
#     async def catch(self, interaction: discord.Interaction):
#         await interaction.response.send_message("You Caught it!")

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.watching, name="The Degenerates of this Server")
    await bot.change_presence(activity=activity)
    #await bot.tree.add_command(FishGroup())
    synced = await bot.tree.sync(guild=discord.Object(guild_id))
    print("Bot is ready")
    print(len(synced))


@bot.tree.command(name='ping', description='Sends jotchua!', guild=discord.Object(id=guild_id))
async def ping(interaction: Interaction):
    await interaction.response.send_message("<:jotchua:992580804188319824>")


@bot.tree.command(name='example', description='g', guild=discord.Object(id=guild_id))
async def example(interaction: Interaction, message1: str) -> None:
    await interaction.response.send_message(message1)


@bot.command(name='stop', help='stops bot')
async def stop(ctx):
    allowed_role1 = discord.utils.get(ctx.guild.roles, name="The Godfather")
    allowed_role2 = discord.utils.get(ctx.guild.roles, name="Untitled")
    if allowed_role1 or allowed_role2 in ctx.author.roles:
        await bot.get_channel(bot_test_channel_id).send("I am getting very sleepy...why is it all turning black...")
        await bot.close()
        

async def load():
    cogs = [f"cogs.{filename[:-3]}" for filename in os.listdir("cogs") if filename.endswith(".py")]
    for cog in cogs:
        await bot.load_extension(cog)
    # for folder in os.listdir('modules'):
    #     if os.path.exists(os.path.join('modules', folder, 'cog.py')):
    #         await bot.load_extension(f'modules.{folder}.cog')


async def main():
    await load()
    await bot.start(os.getenv('TOKEN'))
asyncio.run(main())