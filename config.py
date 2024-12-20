import os
from dotenv import load_dotenv

load_dotenv()

guild_id = int (os.getenv('GUILD_ID'))
gen_channel_id = int (os.getenv('GEN_CHANNEL_ID'))
bot_test_channel_id = int (os.getenv('BOT_TEST_CHANNEL_ID'))