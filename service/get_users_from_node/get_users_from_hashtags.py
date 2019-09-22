from instabot import Bot
import os
import sys
import time

sys.path.append(os.path.join(sys.path[0], "../../"))


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


def getUsersFromHashTag(bot, hashtags):

    try:
        tags = {}
        users = []

        for i in hashtags:
            bot.api.search_tags(i)
            res = bot.api.last_json
            for result in res["results"]:
                tags[result["name"]] = result["media_count"]
        sorted_by_value = sorted(
            tags.items(), key=lambda kv: kv[1], reverse=True)

        usersFoundByHashtag = []
        limitHashtag = 100
        countForLimit = 0

        for tag in sorted_by_value:

            # Limitando o máximo de hashtags em 100
            if countForLimit == limitHashtag:
                break
            else:
                countForLimit = countForLimit = 1

            if tag[1] < 1000:  # Pegando apenas hashtagas com menos de 1000 perfis cada uma
                print('Fazendo busca por {}'.format(tag[0]))
                usersByHashtah = bot.get_hashtag_users(tag[0])
                for v in usersByHashtah:
                    users.append(v)

                colletedData = {"provider": tag[0], "users": users}
                usersFoundByHashtag.append(colletedData)

                time.sleep(1)

        return usersFoundByHashtag

    except:
        return False
