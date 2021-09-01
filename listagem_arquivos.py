from os import listdir
from os.path import isfile, join
import pathlib

mypath = pathlib.Path().resolve()

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

images = []
for i in onlyfiles:
    if "png" in i or "jpg" in i:
        if i != "back.png" and i != "forward.png" and i != "exit.png":
            images.append(i)

print(images)