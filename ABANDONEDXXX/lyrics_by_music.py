"""
根据歌曲 ID 获得所有的歌曲所对应的评论信息
XXX: 网易云音乐歌词内容动态加载
"""

import requests
from bs4 import BeautifulSoup

filein = open('music')

class Comments(object):
    headers = {
        'Host': 'www.azlyrics.com',
        'Connection': 'keep-alive',
        'Content-Length': '484',
        'Cache-Control': 'max-age=0',
        'Origin': 'http://music.163.com',
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OSX 10_13) AppleWebKit/604.1.38(KHTML, likeGecko) Version/11.0 Safari/604.1.38',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'DNT': '1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
        'Cookie': 'JSESSIONID-WYYY=b66d89ed74ae9e94ead89b16e475556e763dd34f95e6ca357d06830a210abc7b685e82318b9d1d5b52ac4f4b9a55024c7a34024fddaee852404ed410933db994dcc0e398f61e670bfeea81105cbe098294e39ac566e1d5aa7232df741870ba1fe96e5cede8372ca587275d35c1a5d1b23a11e274a4c249afba03e20fa2dafb7a16eebdf6%3A1476373826753; _iuqxldmzr_=25; _ntes_nnid=7fa73e96706f26f3ada99abba6c4a6b2,1476372027128; _ntes_nuid=7fa73e96706f26f3ada99abba6c4a6b2; __utma=94650624.748605760.1476372027.1476372027.1476372027.1; __utmb=94650624.4.10.1476372027; __utmc=94650624; __utmz=94650624.1476372027.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    }

    url = 'http://music.163.com/song'

    authen = ('5226dc5a-e3b4-4ab8-b060-b1912ce05c54','Jrz1z5OuFVTj')


    def save_lyrics(self):
        r = requests.get('https://www.azlyrics.com/lyrics/alazka/ghost.html',headers = self.headers)
        soup = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')
        body = soup.body
        lyrics = body.find('div',attrs={'class':'ringtone'}).next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.text

        res = requests.get('https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21', auth=self.authen, params={'text',})



if __name__ == '__main__':
    my_comment = Comments()
#for i in filein:
#       id = i.split()
#        my_comment.save_lyrics(id[0])

    my_comment.save_lyrics()

filein.close()