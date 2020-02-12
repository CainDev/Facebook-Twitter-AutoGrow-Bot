# Modules
import os
import os.path
import subprocess
import random
import time

# Classes
import TwilioClass
song_name = ""


def _check_song_count():
    song_count = 0
    for name in os.listdir("songs"):
        song_count = song_count + 1

    if song_count >= 1:
        return True
    elif song_count == 0:
        TwilioClass.send_message("Out of Songs!")
        return False


def _pick_song():
    song_list = []
    global song_name
    for name in os.listdir("songs"):
        song_list.append(name)

    if len(song_list) == 1:
        cmd_line = 'ffmpeg -i "videos/zeze.mp4" -i "songs"/"{}" -shortest "completed"/"{}".mp4'.format(song_list[0], song_list[0][:-4])
        print("Muxing Video with {}".format(song_list[0][:-4]))
        subprocess.call(cmd_line, shell=False)
        print("Muxing Complete!")

        song_name = song_list[0]
        with open("settings/old-songs.txt", "a+") as songs:
            songs.writelines(song_list[0][:-4] + "\n")
        songs.close()

        #  os.remove("songs/" + song_list[0])
    else:
        random_song = random.randint(0, len(song_list) - 1)
        cmd_line = 'ffmpeg -i "videos/zeze.mp4" -i "songs"/"{}" -shortest "completed"/"{}".mp4'.format(song_list[random_song], song_list[random_song][:-4])
        print("Muxing Video with {}".format(song_list[random_song][:-4]))
        subprocess.call(cmd_line, shell=False)
        print("Muxing Complete!")

        song_name = song_list[random_song]
        with open("settings/old-songs.txt", "a+") as songs:
            songs.writelines(song_list[random_song][:-4] + "\n")
        songs.close()

        #  os.remove("songs/" + song_list[random_song])


def mux_video():
    if _check_song_count():
        _pick_song()
    else:
        print("You're out of songs")
        time.sleep(3)
        exit()