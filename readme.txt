[DISCLAIMER - PLEASE READ THIS!]
I'm going to start off with I am someone who believes HEAVY in project based learning. So that's what this is. I have
used C# for a bit over a year but I'm not very experienced with Python so I have made this to try become more proficient,
so please excuse any coding errors, mistakes or simply things done in-efficiently.

[SUMMARY - PLEASE READ THIS!]
This is a very simple bot that was made to try Auto-Grow a Facebook page. You have already probably seen pages like
this before, below are some examples
;- https://www.facebook.com/109998523716480/
;- https://www.facebook.com/inbetweenersdances/
;- https://www.facebook.com/DisagioAndDepressione/

The bot will take the Video from the 'videos' folder and Mux it with a song from the 'songs' folder. Then proceed to
upload it to your desired Facebook page. I have avoided auto-song finding because I'm almost certain its illegal to make
a bot that pirates music and uploads it so use this at your own discretion.

[Pre-Requisites]
> Python (3.8 or Later - https://www.python.org/downloads/)
> Downloaded Songs (.mp3)
> Downloaded Video (.mp4)
> Facebook Page
> Twilio Account (With Number, Account Credit & Auth)
    > My Referral Link: www.twilio.com/referral/G3HzTH
    > Can be disabled if you aren't interested in SMS updates (TwilioClass.py)
> Ffmpeg (Make sure to set its PATH up correctly)
> You will need to Request "publish_videos" & "manage_pages" API from Facebook's Developer Console
> Common sense, ability to fix issues that arise (Do as the developer do, Google)

[Required Modules]
> Twilio (twilio.rest)
> Requests (requests)

-----

[Set-Up]
> FacebookClass.py
    > Line 27
        > Use your Pages ID/Name in the "url" variable

> Settings Folder
    > twiliosettings.txt (Fill with Your Number, Account SID, Account AUTH & Account Phone Number)
    > facebooksettings.txt (Fill with Your Access Token, App ID, App Secret)
        > How to get a "Long Lived" Token (This is only for testing purposes)
            >Go to https://developers.facebook.com/tools/debug/accesstoken > Input your Current Token > Click Debug > Scroll Down > Click "Extend" > Grab that Token (Should last minimum 2 months, not 1 hour)

> Open CMD
    > Type "pip install twilio"
    > Type "pip install requests"

> Songs
    > Drag .mp3s into this folder.
        > All songs will be saved in old-songs.txt in the [Settings] folder. Just so you know what has been posted.
    > Small hint for you >COPY WHATS SUCCESSFUL<

> Videos
    > Drag .mp4 into this folder.

> Ffmpeg
    > Download from https://www.ffmpeg.org/
        > Include it to Windows Path
