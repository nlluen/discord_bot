# import discord
# from discord.ext import commands, tasks
# import datetime
# import random
# import json
# from config import guild_id, gen_channel_id, worker_role_id
# #from modules import updateHolidays
#
#
# def get_work_message(work_role):
#     message = f"{work_role.mention} Happy 5 PM!"
#     return message
#
#
# def get_morning_messages():
#     message_list = ["Good morning everyone! Have a great day :)", "Rise and grind everyone!"]
#     num = random.randint(0, 1)
#     message = message_list[num]
#     return message
#
#
# class Timed_Messages(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self.daily_messages.start()
#         self.birthday_messages.start()
#
#     # @commands.cooldown(1, 1, commands.BucketType.user)
#     @tasks.loop(seconds=50)
#     async def daily_messages(self):
#         date = datetime.datetime.now()
#         hour = date.hour
#         minute = date.minute
#         gen_channel = self.bot.get_channel(gen_channel_id)
#         if gen_channel:
#             if hour == 8 and minute == 00:
#                 morning_message = get_morning_messages()
#                 await gen_channel.send(date.strftime(f"{morning_message} Today is %B %d, %Y"))
#                 # days = updateHolidays()
#                 embed = discord.Embed(title="Here Are The Fun Holidays For Today")
#                 # for holiday in days:
#                 #     embed.add_field(name='\n', value=f'{holiday}\n', inline=False)
#                 # await gen_channel.send(embed=embed)
#             if hour == 16 and minute == 20:
#                 await gen_channel.send("420")
#             if hour == 17 and minute == 00:
#                 if date.weekday() < 5:
#                     work_role = self.bot.get_guild(guild_id).get_role(worker_role_id)
#                     work_message = get_work_message(work_role)
#                     await gen_channel.send(work_message)
#             if hour == 23 and minute == 11:
#                 await gen_channel.send("11:11 make a wish")
#             if hour == 23 and minute == 30:
#                 await gen_channel.send("Getting sleepy... Goodnight everyone see you all tomorrow. Sweet dreams :)")
#         else:
#             print('no work')
#
#     @tasks.loop(seconds=40)
#     async def birthday_messages(self):
#         date = datetime.datetime.now()
#         todays_month = date.month
#         todays_day = date.day
#         with open('members.json', 'r') as rf:
#             members = json.load(rf)
#         for member_id in members:
#             birthday_month, birthday_day = map(int, members[member_id]["Birthday"].split('/'))
#             if todays_month == birthday_month and todays_day == birthday_day:
#                 if date.hour == 00 and date.minute == 5:
#                     gen_channel = self.bot.get_channel(gen_channel_id)
#                     if gen_channel:
#                         member = self.bot.get_guild(guild_id).get_member(int (member_id))
#                         color = members[member_id]["Color"]
#                         em = discord.Embed(title="Happy Birthday", color=discord.Color.from_str(color))
#                         em.description = f"Today is <@{member_id}>'s birthday! Everyone wish them a happy birthday :D"
#                         pfp = member.display_avatar
#                         em.set_thumbnail(url=f'{pfp}')
#                         await gen_channel.send(embed=em)
#
#
#
#     @birthday_messages.before_loop
#     @daily_messages.before_loop
#     #@water_reminder.before_loop
#     async def before_water_reminder(self):
#         await self.bot.wait_until_ready()
#
#
# async def setup(bot):
#     await bot.add_cog(Timed_Messages(bot))