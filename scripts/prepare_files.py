import os
from tinytag import TinyTag

mp3_files = [x for x in os.listdir("../") if x.endswith(".mp3")]
mp3_files = sorted(mp3_files)

available_files_location = "../available.txt"

batch_content = ""

for mp3 in mp3_files:
    title = os.path.basename("../" + mp3)

    tag = TinyTag.get('../' + mp3)

    sample_rate = tag.samplerate
    
    print("title: {} sample_rate: {}".format(title, sample_rate))

    filesize = tag.filesize / 1024

    mins = int(tag.duration / 60)
    seconds = tag.duration

    duration = "{:02d} mins {:02d} secs".format(mins, int(seconds - mins * 60))

    batch_content += "{}, {}, {}, {}\n".format(title, mp3, round(filesize), duration)

with open(available_files_location, "w") as available_file:
    available_file.write(batch_content)
