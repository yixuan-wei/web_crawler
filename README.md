![](https://img.shields.io/badge/Python-3.5.2-blue.svg)

这是一个爬取网易云音乐的所有的歌曲的爬虫。

以下为主要思路：

1. 爬取所有的歌手信息（[artists.py](music_163/artists.py)）；
2. 根据上一步爬取到的歌手信息去爬取所有的专辑信息（[album_by _artist.py](music_163/album_by_artist.py)）；
3. 根据专辑信息爬取所有的歌曲信息（[music_by _album.py](music_163/music_by_album.py)）；

