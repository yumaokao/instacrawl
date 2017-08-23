#!/usr/bin/env python
import argparse
from tqdm import tqdm
from instabot import Bot


read_userids = []


def crawler(bot, user_id):
    medias = bot.get_user_medias(user_id)
    username = bot.get_username_from_userid(user_id)
    followings = bot.get_user_following(user_id)
    print('{} {} has {} medias {} followings'.format(username, user_id, len(medias), len(followings)))
    read_userids.append(user_id)
    # bot.download_photos(medias)
    for f in followings:
        if f not in read_userids:
            crawler(bot, f)

class CrawlerBot(Bot):
    def __init__(self):
        super().__init__()


def main():
    parser = argparse.ArgumentParser(description='insta')
    parser.add_argument('-u', '--username', help="username")
    parser.add_argument('-p', '--password', help="password")
    parser.add_argument('--proxy', help="proxy")
    # parser.add_argument('hashtags', type=str, nargs='+', help='hashtags')
    args = parser.parse_args()

    bot = CrawlerBot()
    bot.login(username=args.username, password=args.password)

    user_id = bot.get_userid_from_username('yumaokao')
    crawler(bot, user_id)

    '''
    for hashtag in args.hashtags:
        medias = bot.get_hashtag_medias(hashtag)
        print(medias)
    user_id = bot.get_userid_from_username('yumaokao')
    followings = bot.get_user_following(user_id)
    print(user_id)
    print(followings)
    '''


if __name__ == "__main__":
    main()
