import os

import tweepy
from time import sleep

# Classes
import MuxingClass

# Global Variables
authorisation_information = []


def initial_setup():
    global authorisation_information
    with open("settings/twittersettings.txt", "r") as settings:
        information = settings.readlines()
        for line in information:
            authorisation_information.append(line.split("=")[1])
    settings.close()


def OAuth():
    try:
        auth = tweepy.OAuthHandler(authorisation_information[0].strip(), authorisation_information[1].strip())
        auth.set_access_token(authorisation_information[2].strip(), authorisation_information[3].strip())
        return auth
    except Exception as e:
        return None


initial_setup()
Api = tweepy.API(OAuth())


def post_video():
    uploaded = False

    if not uploaded:
        print("Uploading Video...")
        upload_result = Api.media_upload("completed/{}.mp4".format(MuxingClass.song_name[:-4]))

        print("Video uploaded, waiting for processing...")
        uploaded = True
        sleep(15)

    try:
        print("Trying to post video now...")
        Api.update_status(status="{} \n\n"
                                 "#FreeKodakBlack "
                                 "#KodakBlack".format(MuxingClass.song_name[:-4]),
                          media_ids=[upload_result.media_id_string]
                          )
        print("Video Posted!")
        uploaded = False
    except Exception as e:
        print("Twitter is still processing the video, sleeping for 15 seconds then trying again...")
        post_video()
