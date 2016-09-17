#get data from GPMDP
#load lyrics
# record time on button press
#save to json

import os;
import json;

song_info = json.loads(open('C:\Users\Jack\AppData\Roaming\Google Play Music Desktop Player\json_store\playback.json','r').read())
song_title = song_info["song"]['title']

print('Loading \'' + song_title + '\' lyrics...')

try:
    f = open('../lyrics/{0}.txt'.format(song_title),'r')

    lyriclines = f.read().split('\n')

    for i in range(0,len(lyriclines)):
        print("{0}| {1}".format(i,lyriclines[i]))
        
except (IOError) as ex:
    if ex.errno == 2:
        print('ERROR: No lyrics file found')