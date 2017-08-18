#!/usr/bin/env python
from instagram.client import InstagramAPI


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
    client_id = 'eda84a8c2e614e1d848a669b0cbbc1ef'          # user your client id
    client_secret = '1435907e959e4920bb077bc9475aed02'      # user your client secret id
    redirect_uri = 'http://localhost'                       # user your redirect_uri

    client = Insta(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    client.access_token()


if __name__ == "__main__":
    main()
