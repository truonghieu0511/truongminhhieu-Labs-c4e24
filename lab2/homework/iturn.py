from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
page_content = raw_data.decode("utf-8")
soup = BeautifulSoup(page_content, "html.parser")
div = soup.find("div", id = "main")
ul = div.section.div.ul
li_list = ul.find_all("li")
songs_list = []
for li in li_list:
    h3 = li.h3.a
    h4 = li.h4.a
    song = h3.string
    artist = h4.string
    songs = OrderedDict({
        "song": song,
        "artist": artist
    })
    songs_list.append(songs)

pyexcel.save_as(records=songs_list, dest_file_name="itunes.xlsx")
options = {
    "default_search" : "ytsearch",
    "format" : "bestaudio/audio"
    
   
}
dl = YoutubeDL(options)

for topsong in songs_list:
    dl.download([topsong["song"] + topsong["artist"]])