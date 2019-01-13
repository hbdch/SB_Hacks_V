# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACebcbe9c9d5edc1ce90656251f0a9ba65'
auth_token = '815eb047f5e29ad2904d3ce1230a8107'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='https://12f4131f.ngrok.io/voice',
                        to='+14086379521',
                        from_='+14088726871'
                    )

print(call.sid)