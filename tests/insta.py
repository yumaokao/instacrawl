#!/usr/bin/env python
import argparse
from instabot import Bot


class Insta:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri

    def access_token(self):
        scope = ['basic']
        self.api = InstagramAPI(client_id = self.client_id, client_secret = self.client_secret, redirect_uri = self.redirect_uri)
        redirect_uri = self.api.get_authorize_login_url(scope = scope)
        print(redirect_uri)

        code = (str(input("Paste in code in query string after redirect: ").strip()))
        self.access_token = self.api.exchange_code_for_access_token(code)
        print(self.access_token)

        return self.access_token


def main():
    parser = argparse.ArgumentParser(description='insta')
    parser.add_argument('-u', '--username', help="username")
    parser.add_argument('-p', '--password', help="password")
    parser.add_argument('--proxy', help="proxy")
    parser.add_argument('hashtags', type=str, nargs='+', help='hashtags')
    args = parser.parse_args()

    bot = Bot()
    bot.login(username=args.username, password=args.password)

    '''
    for hashtag in args.hashtags:
        medias = bot.get_hashtag_medias(hashtag)
        print(medias)
    '''
    user_id = bot.get_userid_from_username('yumaokao')
    followings = bot.get_user_following(user_id)
    print(user_id)
    print(followings)


if __name__ == "__main__":
    main()
