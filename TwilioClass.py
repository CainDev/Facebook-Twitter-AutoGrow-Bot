from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

account_information = []
sms_initiated = True
send_messages = True  # Set to false if you want to disable Twilio


def _first_time_run():
    global account_information
    global sms_initiated
    with open("settings/twiliosettings.txt", "r") as settings:
        private_information = settings.readlines()
        for line in private_information:
            account_information.append(line.split("=")[1])
    settings.close()

    try:
        client = Client(account_information[0], account_information[1])
        print("Starting Balance: " + client.balance.fetch().currency + " " + client.balance.fetch().balance)
        sms_initiated = True
    except TwilioRestException as e:
        if e.status == 401:
            print("Please check your Twilio Account [SID] & [AUTH TOKEN].")
            print("Disabling Twilio updates to prevent bot from crashing...")
            sms_initiated = False
        else:
            print("Unexpected Twilio Error")
            print("Disabling Twilio updates to prevent bot from crashing...")
            sms_initiated = False


def send_message(message_body):
    global send_messages
    if send_messages:
        _first_time_run()
        if sms_initiated:
            try:
                client = Client(account_information[0], account_information[1])
                client.messages.create(to=account_information[2], from_=account_information[3], body=message_body)
            except TwilioRestException as e:
                if e.status == 404:
                    print("Either your [TWILIO PHONE NUMBER] or [YOUR PHONE NUMBER] are incorrect. Please double check.")
                    print("Disabling Twilio updates to prevent bot from crashing...")
                    send_messages = False
                else:
                    print(e.code)
                    print("Unexpected Twilio Error")
                    print("Disabling Twilio updates to prevent bot from crashing...")
                    send_messages = False
