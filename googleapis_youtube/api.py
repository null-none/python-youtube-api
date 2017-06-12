import requests, json


class YoutubeAPI(object):

    def __init__(self, api):
        self.api = api
        self.url = 'https://www.googleapis.com/youtube/v3/'

    def videos_channel(self, params):
        url = '{0}activities?part=snippet,contentDetails&channelId={1}&maxResults=12&key={2}'.format(self.url, params, self.api)
        result = requests.get(url)
        return result.json()

    def information_channels(self, params):
        url = '{0}channels?part=snippet&forUsername={1}&key={2}'.format(self.url, params, self.api)
        result = requests.get(url)
        return result.json()

    def playlist(self, params):
        url = '{0}playlistItems?part=snippet&playlistId={1}&key={2}'.format(self.url, params, self.api)
        result = requests.get(url)
        return result.json()
