from __future__ import unicode_literals

import os
import sys

from tqdm import tqdm

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402


bot = Bot()
bot.login(username='afonsoclaudio8888', password='lara199999')


def dispositions(l):
    from itertools import permutations

    print("Generating dispositions...")
    res = []
    res += [a for a in l]
    length = len(l)
    num = 2
    while num <= length:
        p = list(permutations(l, num))
        res += [" ".join(c) for c in p]
        num += 1
    print("Generated {} dispositions".format(len(res)))
    return res


tags = {}
users = []
hashtags = ['vitoria', 'ufes']
for i in hashtags:  # tqdm(dispositions(sys.argv[1:])):
    bot.api.search_tags(i)
    res = bot.api.last_json
    for result in res["results"]:
        tags[result["name"]] = result["media_count"]
sorted_by_value = sorted(tags.items(), key=lambda kv: kv[1], reverse=True)

bot.logger.info("Found {} hashtags".format(len(sorted_by_value)))
for tag in sorted_by_value:
    usersByHashtag = bot.get_hashtag_users()
