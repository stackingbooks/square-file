# encoder.py [data file path] [output file path]

from pydub import playback, audio_segment, generators
import sys
import os
import time

a = []
au = audio_segment.AudioSegment.empty()

freqs = {
    "0": 400,
    "1": 430,
    "2": 460,
    "3": 490,
    "4": 510,
    "5": 540,
    "6": 570,
    "7": 600,
    "8": 630,
    "9": 660,
    "a": 690,
    "b": 720,
    "c": 750,
    "d": 780,
    "e": 810,
    "f": 840
}
string = b""
i = 0
m = time.time()
with open(sys.argv[1], "rb") as f:
    string = f.read()
    f.close()
j = len(string)
for l in string:
    o = l
    hx = hex(o)
    hx = hx.replace("0x","")
    if len(hx)==1:
        hx = "0"+hx
    if len(hx)==3:
        hx = "0"+hx
    if len(hx)==5:
        hx = "0"+hx
    i += 1
    if i%200==0:
        k = str(i)
        l = str(j)
        os.system('cls')
        print("generating:")
        print('('+k+"/"+l+')')
        print(str(200/(time.time()-m)) + " bytes/s")
        m = time.time()
    for h in hx:
        a.append(generators.Square(freqs[h]).to_audio_segment(10,0))

# playback.play(a)
i = 0
m = time.time()
j = len(a)
for b in a:
    au = au+b
    i += 1
    if i%200==0:
        k = str(i/2)
        l = str(j/2)
        os.system('cls')
        print("exporting:")
        print('('+k+"/"+l+')')
        print(str((200/(time.time()-m))/2) + " byte/s")
        m = time.time()
au.export(sys.argv[2], "wav")
os.system('cls')
k = str(i)
l = str(j)
print("done, ("+k+"/"+l+'), saved to '+sys.argv[2])