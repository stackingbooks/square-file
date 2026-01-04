# decoder.py [encoded audio file path] [output file path]

from pydub import playback, audio_segment, generators, utils
import array
import math
import sys
import time
import os

a = audio_segment.AudioSegment.from_file(sys.argv[1])

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

result = []
result2 = []
h = array.array("h")
h.frombytes(a.raw_data)
y = 44100*0.01
i = 0
m = time.time()
aa = math.floor((44100*a.duration_seconds)/y)
for i in range(math.floor((44100*a.duration_seconds)/y)):
    start = int(i*y)
    end = int(start+y)
    j = h[start:end]
    c = 0
    e = 0
    for v in j:
        w = v
        if w>0:
            c += 1
        else:
            break
    if (c==0):
        e = 0
    else:
        e = 44100/(c/0.5)
    result.append(e+10)
    i += 1
    if i%200==0:
        k = str(i/2)
        l = str(aa/2)
        os.system('cls')
        print("calculating:")
        print('('+k+"/"+l+')')
        print(str((200/(time.time()-m))/2) + " byte/s")
        m = time.time()

i = 0
m = time.time()
j = len(result)
for r in result:
    i += 1
    nearest = ""
    n2 = 999
    for f in freqs.keys():
        t = r-freqs[f]
        if (t<0):
            t = t*-1
        if n2 > t:
            nearest = f
            n2 = t
    result2.append(nearest)
    if (i%2==0):
        result2.append(" ")
    if i%200==0:
        k = str(i/4)
        l = str(j/2)
        os.system('cls')
        
        print("estimating:")
        print('('+k+"/"+l+')')
        print(str((200/(time.time()-m))/2) + " byte/s")
        m = time.time()

os.system('cls')
print("exporting...") 
with open(sys.argv[2], "xb") as f:
    for c in ("".join(result2)).split(" "):
        if len(c)==2:
            f.write(bytes.fromhex(c))
    f.close()
    