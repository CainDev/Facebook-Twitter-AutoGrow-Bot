# Modules
import os
import os.path
import time
from datetime import datetime
from datetime import timedelta

# Classes
import MuxingClass
import TwilioClass
import FacebookClass

# Global Variables
bot_running = True
post_delay = 7200



def calculate_remaining_posts():
    number_of_songs = len(os.listdir("songs"))

    if number_of_songs == 0:
        print("Add songs to the song folder please.")
        time.sleep(3)
        exit()

    total_seconds = post_delay * number_of_songs
    total_minutes = total_seconds / 60
    total_hours = total_minutes / 60

    predicted_expiry = (datetime.now() + timedelta(hours=total_hours) - datetime.now())
    print("Bot will run for: " + str(predicted_expiry) + " (HH:MM:SS)")


def main_bot():
    # Calculate
    calculate_remaining_posts()

    # Mux Video
    MuxingClass.mux_video()

    # Post Video
    FacebookClass.post_video()

    # Delete Video
    #  FacebookClass.delete_video()

    # Sleep
    print("Sleeping for {} minutes.".format(str((post_delay / 60))))
    time.sleep(post_delay)

    main_bot()


while bot_running:
    main_bot()
