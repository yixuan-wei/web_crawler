"""
根据azlyrics.com上的歌词，ibm tone analyzer 得到歌词情感分析
"""

import requests
import requests.adapters
from bs4 import BeautifulSoup
import bs4

out = open('data', 'w')
requests.adapters.DEFAULT_RETRIES = 5
headers = {
    'Host': 'www.azlyrics.com',
    'Connection': 'close',
    'Content-Length': '484',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://www.azlyrics.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}


class Lyrics(object):
    headers1 = {
        'Content-Type': 'text/plain',
        'charset': 'utf-8'
    }

    authen = ('5226dc5a-e3b4-4ab8-b060-b1912ce05c54', 'Jrz1z5OuFVTj')

    def save_lyrics(self, song_name):
        r = requests.get('https://www.azlyrics.com/lyrics/' + song_name, headers=headers, params={'limit': '100'})
        soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')
        body = soup.body
        song_names = body.find('div', attrs={'class': 'ringtone'}).next_sibling.next_sibling
        lyrics = song_names.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text
        lyric = lyrics.encode()
        res = requests.post('https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21',
                            auth=self.authen, data=lyric, headers=self.headers1)
        result = res.text
        song_tone = []
        for i in range(0, 2):
            song_tone.append(result["document_tone"]["tones"][i])
        return lyrics, song_tone


def save_artists(letter_id):
    r = requests.get('https://www.azlyrics.com/' + letter_id + '.html', headers=headers, params={'limit': '100'})
    soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')
    body = soup.body
    artists_names = body.find('div', attrs={'class': 'col-sm-6 text-center artist-col'}).descendants
    artist_url = []
    for artist_name in artists_names:
        if type(artist_name) == bs4.element.Tag:
            if artist_name.name == 'a':
                artist_url.append("'"+artist_name['href']+"'")
    return artist_url


def find_song_name(artist_url):
    r = requests.get('https://www.azlyrics.com/' + artist_url, headers=headers, params={'limit': '100'})
    soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')
    body = soup.body
    songs_names = body.find_all('a', attrs={'target': "_blank"})
    song_names = []
    for piece in songs_names:
        result = piece['href']
        name = piece.children
        print(name)
        song_names.append([result[10:], name])
    return song_names


if __name__ == '__main__':
    out.write('{')
    artist_url = []
    artist_url.append(save_artists('19'))
    for i in range(ord('a'), ord('z') + 1):
        id = chr(i)
        artist_url = artist_url + save_artists(id)
    for i in artist_url:
        song_names = []
        song_names = find_song_name(i)
        my_lyric = Lyrics()

        for j in song_names:
            lyric = []
            tone = []
            lyric, tone = my_lyric.save_lyrics(j[0])
            out.write('[' + j[1] + ", [" + ",".join(tone) + "], " + lyric + ']')
    out.write("}")
    out.close()
