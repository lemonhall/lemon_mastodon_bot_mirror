from mastodon import Mastodon

mastodon = Mastodon(
    access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    api_base_url = 'https://cmx-im.work/'
)

mastodon.toot('Tooting from python using #mastodonpy !')