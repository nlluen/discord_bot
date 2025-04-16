import os
from dotenv import load_dotenv

load_dotenv()

guild_id = int(os.getenv('GUILD_ID'))
announcement_channel_id = int(os.getenv('ANNOUNCEMENT_CHANNEL_ID'))
gen_channel_id = int(os.getenv('GEN_CHANNEL_ID'))
bot_test_channel_id = int(os.getenv('BOT_TEST_CHANNEL_ID'))
worker_role_id = int(os.getenv('WORKER_ROLE_ID'))
welcome_channel_id = int(os.getenv('WELCOME_CHANNEL_ID'))
mod_role_id = int(os.getenv('MOD_ROLE_ID'))
admin_role_id = int(os.getenv('ADMIN_ROLE_ID'))
godmother_role_id = int(os.getenv('GODMOTHER_ROLE_ID'))
