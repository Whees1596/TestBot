import os
from dotenv import load_dotenv
from os import getenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = tuple(map(int, getenv('ADMINS').split(',')))


ip = os.getenv("ip")
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'