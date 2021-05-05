from __future__ import unicode_literals
import youtube_dl
import os
import random

name = input("Please enter File Name: ")
youtube_url = input("Please enter youtube Url: ")
startTimeMin = input("Please enter start time Min: ")
startTimeSecond = input("Please enter start time Sec: ")
endTimeMin = input("Please enter end time Min: ")
endTimeSecond = input("Please enter end time Sec: ")

startTimeMin = int(startTimeMin)
startTimeSecond = int(startTimeSecond)
endTimeMin = int(endTimeMin)
endTimeSecond = int(endTimeMin)



ydl_opts = {
    'outtmpl': name+'.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([youtube_url])



from pydub import AudioSegment

startMin = startTimeMin
startSec = startTimeSecond

endMin = endTimeMin
endSec = endTimeSecond

# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000

introRandom = str(random.randint(0, 1))


# Opening file and extracting segment
song = AudioSegment.from_mp3(name+'.mp3')
intro = AudioSegment.from_mp3('Intros/'+introRandom+'.mp3')
extract = song[startTime:endTime]

combined = intro.append(extract)

combined.export(name+'-edited.mp3', format="mp3")
