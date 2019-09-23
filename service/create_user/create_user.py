from instabot import Bot
import os
import sys


sys.path.append(os.path.join(sys.path[0], "../../"))


def createNewUser(bot):
    userId = bot.user_id
    username = bot.username

    whoIFollow = bot.get_user_following(userId)
    whoFollowMe = bot.get_user_followers(userId)

    user = {'_id': userId, 'username': username,
            'whoIFollow': whoIFollow, 'whoFollowMe': whoFollowMe}

    return user
