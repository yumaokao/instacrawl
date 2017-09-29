#!/usr/bin/env python
import argparse
from tqdm import tqdm
from instabot import Bot


class CrawlerBot(Bot):
    def __init__(self):
        super().__init__()
        self.read_userids = []
        self.queued_userids = []

    def download_photos(self, medias, path='photos/', description=False):
        broken_items = []
        if len(medias) == 0:
            self.logger.info("Nothing to downloads.")
            return broken_items
        self.logger.info("Going to download %d medias." % (len(medias)))
        for media in tqdm(medias):
            if not self.download_photo(media, path, filename=media, description=description):
                delay.error_delay(self)
                broken_items = medias[medias.index(media):]
                break
        return broken_items

    def crawler_from_username(self, username):
        userid = self.get_userid_from_username(username)
        self.queued_userids.append(userid)

        while True:
            if len(self.queued_userids) == 0:
                break
            userid = self.queued_userids.pop(0)
            self.crawler(userid)

    def crawler(self, userid):
        try:
            medias = self.get_user_medias(userid)
            username = self.get_username_from_userid(userid)
            followings = self.get_user_following(userid)
            self.logger.info('{} {} has {} medias {} followings'.format(username, userid, len(medias), len(followings)))
            self.read_userids.append(userid)
            self.download_photos(medias)
        except:
            return
        for u in followings:
            if u not in self.read_userids and u not in self.queued_userids:
                self.queued_userids.append(u)


def main():
    parser = argparse.ArgumentParser(description='insta')
    parser.add_argument('-u', '--username', help="username")
    parser.add_argument('-p', '--password', help="password")
    parser.add_argument('--proxy', help="proxy")
    # parser.add_argument('hashtags', type=str, nargs='+', help='hashtags')
    args = parser.parse_args()

    bot = CrawlerBot()
    bot.login(username=args.username, password=args.password)

    bot.crawler_from_username(args.username)


if __name__ == "__main__":
    main()
