![](https://img.shields.io/badge/Python-3.5.2-blue.svg)

Based on a former 爬取网易云音乐的所有的歌曲的爬虫 developed by the original author.

Inside the ABANDONEDXXX :
1. 爬取所有的歌手信息（[artists.py](music_163/artists.py)）；
2. 根据上一步爬取到的歌手信息去爬取所有的专辑信息（[album_by _artist.py](music_163/album_by_artist.py)）；
3. 根据专辑信息爬取所有的歌曲信息（[music_by _album.py](music_163/music_by_album.py)）；

But eventually it turned out that 163 music utilize active html technology, thus lyrics couldn't be successfully attained through such simple technology.

Found another non-active lyric sites: www.azlyrics.com on the web, trying to attain data.

But IP has already been constrained before I debugged completely.

This web crapper is An unfinished program.

The following steps, including analyzing lyric tunes and matching input text with songs, are in the other reporsitory: sentiment_analysis https://github.com/yixuan-wei/sentiment-analysis.git
