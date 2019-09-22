from instabot import Bot
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../../"))


def getUsersFollowers(bot, userId):
    try:
        followersByUsers = bot.get_user_followers(userId, nfollows=10000)
        return followersByUsers
    except:
        return False


def getUserFollowing(bot, userId):
    try:
        userFollowing = bot.get_user_following(userId)
        return userFollowing
    except:
        return False
