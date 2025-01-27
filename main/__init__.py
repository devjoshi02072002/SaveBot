#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("27944955", default=None, cast=int)
API_HASH = config("2e045584d56a1c086d4091a1b02eb36f", default=None)
BOT_TOKEN = config("8186269324:AAH9ZzoGaT1dHiMaajRZVRc9irFTnNejrXE", default=None)
SESSION = config("BQFfhFEAbVgLQW0DWwdpv7QAiPH1LPB3IqIT3Hf3IpzfMq6j1CtbJluP6Q83vhGge31E06YMYkBO0LrZiavlNAh_eoZVYXg4yr4WT9xRlk5TXodeQSGbDJpJ52Go-u8Matuhv_R9NPkTZZC7Hr25JD5RBThyffPlmwXpsJj-SF4cg7uNF51kzEQQp62Syurm_HU0wIQZBBExPJ9NlyDnjpEADbNabNVk__ppKgJCsf-j4NGGneuBa18dwYfAJMnrSRsfHlWCRbOOyoImF74aIevJ3HTOVqi-kEMjj1BMPeV2-bO_Smq1ulzdW3BsKXOa6kb4qb4Ltl1T4YYqoiCdETug8XZfugAAAABRtBDvAA ", default=None)
FORCESUB = config("hellopriye", default=None)
AUTH = config("1370755311", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
