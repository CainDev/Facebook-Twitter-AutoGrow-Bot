# Modules
import facebook
import requests
import json
import os.path

# Classes
import MuxingClass

# Global Variables
authorisation_information = []


def initial_setup():
    global authorisation_information
    with open("settings/facebooksettings.txt", "r") as settings:
        information = settings.readlines()
        for line in information:
            authorisation_information.append(line.split("=")[1])
    settings.close()


def post_video():
    initial_setup()

    try:
        print("Posting Song...")  # VV Replace with your Graph Link
        url = "https://graph-video.facebook.com/KodakDancin/videos" + \
              "?description={}".format(MuxingClass.song_name[:-4]) + \
              "&title={}".format(MuxingClass.song_name[:-4]) + \
              "&access_token=" + authorisation_information[0]

        video_path = 'completed/{}.mp4'.format(MuxingClass.song_name[:-4])
        files = {'file': open(video_path, 'rb')}
        requests.post(url, files=files)
        print("Song Posted!")
    except Exception as e:
        print(e)


def comment_under_video():
    print("WIP")


def delete_all_posts():
    fb = facebook.GraphAPI(access_token=authorisation_information[0])
    url = "https://graph.facebook.com/v5.0/me?fields=videos%7Bid%7D&access_token=" + authorisation_information[0]
    response = requests.get(url).text
    data = json.loads(response)
    for line in data['videos']['data']:
        fb.delete_object(line['id'])
        print(line['id'] + " Deleted...")
