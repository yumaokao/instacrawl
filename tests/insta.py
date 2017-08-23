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


class Crawler():
    def __init__(self):
        self.bot = Bot()
        self.read_userids = []


    def login(self, username='', password=''):
        self.bot.login(username=username, password=password)

    def crawler_from_username(self, username):
        user_id = self.bot.get_userid_from_username(username)
        self.crawler(user_id)

    def crawler(self, user_id):
        medias = self.bot.get_user_medias(user_id)
        username = self.bot.get_username_from_userid(user_id)
        followings = self.bot.get_user_following(user_id)
        self.bot.logger.info('{} {} has {} medias {} followings'.format(username, user_id, len(medias), len(followings)))
        self.download_photos(medias)

    def download_photos(self, medias, path='photos/'):
        broken_items = []
        if len(medias) == 0:
            self.bot.logger.info("Nothing to downloads.")
            return broken_items
        self.bot.logger.info("Going to download %d medias." % (len(medias)))
        for media in tqdm(medias):
            if not self.bot.download_photo(media, path):
                # delay.error_delay(self)
                broken_items = medias[medias.index(media):]
                break
        return broken_items


def main():
    parser = argparse.ArgumentParser(description='insta')
    parser.add_argument('-u', '--username', help="username")
    parser.add_argument('-p', '--password', help="password")
    parser.add_argument('--proxy', help="proxy")
    # parser.add_argument('hashtags', type=str, nargs='+', help='hashtags')
    args = parser.parse_args()

    bot = Crawler()
    bot.login(username=args.username, password=args.password)

    bot.crawler_from_username('yumaokao')
    # user_id = bot.get_userid_from_username('yumaokao')
    # crawler(bot, user_id)

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
