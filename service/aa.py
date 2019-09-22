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

a = bot.get_locations_from_coordinates(latitude=-20.1910, longitude=-40.2016)

users = []

tags = {}

hashtags = ['vitoria', 'ufes']
for i in hashtags:  # tqdm(dispositions(sys.argv[1:])):
    bot.api.search_tags(i)
    res = bot.api.last_json
    for result in res["results"]:
        tags[result["name"]] = result["media_count"]
sorted_by_value = sorted(tags.items(), key=lambda kv: kv[1], reverse=True)

bot.logger.info("Found {} hashtags".format(len(sorted_by_value)))

ss = 0
for tag in sorted_by_value:
    if tag[1] < 1000:
        ss = ss + 1
print('abd e {}'.format(ss))
for tag in sorted_by_value:
    if tag[1] < 1000:
        print('Fazendo busca por {}'.format(tag[0]))
        usersByHashtah = bot.get_hashtag_users(tag[0])
        for v in usersByHashtah:
            users.append(v)
        time.sleep(1)
        print(users)
        print(len(users))
qq = set(users)
print(qq)
print(len(qq))


"""
print(type(a))
q = 0
for i in a:
    w = i['location']
    q = q + 1
    print('{} - {}'.format(q, w['name']))
"""
