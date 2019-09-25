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

timeSleepInMs = random.uniform(11, 25)

print(timeSleepInMs)

"""
bot = Bot(filter_private_users=False)
bot.login(username='gatopagina', password='lara1999')


bot.send_message(
    "estou fazendo uma campanha para as pessoas usarem mais o google. Apenas isso. www.google.com", "7071041047")
"""
