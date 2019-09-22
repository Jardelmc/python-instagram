from instabot import Bot
import argparse
import requests
import os
import sys
import json
import random
import time
import datetime


sys.path.append(os.path.join(sys.path[0], "../"))
parser = argparse.ArgumentParser(add_help=True)
args = parser.parse_args()

bot = Bot(filter_private_users=False)
bot.login(username='afonsoclaudio8888', password='lara199999')

a = bot.user_id

print(a)
