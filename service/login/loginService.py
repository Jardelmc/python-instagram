from instabot import Bot
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../../"))


def init(username, password):
    try:
        os.mkdir('./payload')
        os.mkdir('./payload/{}'.format(username))
    except:
        pass

    whitelist_file = "./payload/{}/whitelist.txt".format(username)
    blacklist_file = "./payload/{}/blacklist.txt".format(username)
    comments_file = "./payload/{}/comments.txt".format(username)
    followed_file = "./payload/{}/followed.txt".format(username)
    unfollowed_file = "./payload/{}/unfollowed.txt".format(username)
    skipped_file = "./payload/{}/skipped.txt".format(username)
    friends_file = "./payload/{}/friends.txt".format(username)

    max_likes_per_day = 198
    max_follows_per_day = 198
    max_messages_per_day = 20
    filter_users_without_profile_photo = True
    filter_business_accounts = True
    filter_verified_accounts = True
    min_media_count_to_follow = 4
    stop_words = ('loja')
    blacklist_hashtags = ["#loja"]
    blocked_actions_protection = True
    verbosity = True

    bot = Bot(filter_private_users=False,
              whitelist_file=whitelist_file,
              blacklist_file=blacklist_file,
              comments_file=comments_file,
              followed_file=followed_file,
              unfollowed_file=unfollowed_file,
              skipped_file=skipped_file,
              friends_file=friends_file,
              max_likes_per_day=max_likes_per_day,
              max_follows_per_day=max_follows_per_day,
              max_messages_per_day=max_messages_per_day,
              filter_users_without_profile_photo=filter_users_without_profile_photo,
              filter_business_accounts=filter_business_accounts,
              filter_verified_accounts=filter_verified_accounts,
              min_media_count_to_follow=min_media_count_to_follow,
              stop_words=stop_words,
              blacklist_hashtags=blacklist_hashtags,
              blocked_actions_protection=blocked_actions_protection,
              verbosity=verbosity)

    try:
        isLogged = bot.login(username=username, password=password)
        if isLogged == True:
            return bot
        else:
            return False

    except:
        return False
