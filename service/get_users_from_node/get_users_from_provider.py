from instabot import Bot
import os
import sys

from get_users_from_node import get_users

sys.path.append(os.path.join(sys.path[0], "../../"))


def getUsersByUsername(bot, usernameToFind):
    userId = bot.convert_to_user_id(usernameToFind)

    followersList = get_users.getUsersFollowers(bot, userId)

    return followersList
