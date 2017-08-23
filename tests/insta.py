#!/usr/bin/env python
import argparse
from tqdm import tqdm
from instabot import Bot


class CrawlerBot(Bot):
    def __init__(self):
        super().__init__()
        self.read_userids = []

    def crawler_from_username(self, username):
        userid = self.get_userid_from_username(username)
        self.crawler(userid)

    def crawler(self, userid):
        medias = self.get_user_medias(userid)
        username = self.get_username_from_userid(userid)
        followings = self.get_user_following(userid)
        self.logger.info('{} {} has {} medias {} followings'.format(username, userid, len(medias), len(followings)))
        self.read_userids.append(userid)
        self.download_photos(medias)
        for u in followings:
            if u not in read_userids:
                self.crawler(u)


def main():
    parser = argparse.ArgumentParser(description='insta')
    parser.add_argument('-u', '--username', help="username")
    parser.add_argument('-p', '--password', help="password")
    parser.add_argument('--proxy', help="proxy")
    # parser.add_argument('hashtags', type=str, nargs='+', help='hashtags')
    args = parser.parse_args()

    bot = CrawlerBot()
    bot.login(username=args.username, password=args.password)

    bot.crawler_from_username('yumaokao')


if __name__ == "__main__":
    main()
