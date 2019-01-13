from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

test = "50th"
text2 = "To infinity, and beyond!"

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls and mention the caller's city"""
    # Get the caller's city from Twilio's request to our app
    city = request.values['FromCity']

    # Start our TwiML response
    resp = VoiceResponse()


    # Read a message aloud to the caller
    resp.say('Your results are in.', voice='alice')
    resp.say('Your emotional range is in the , {} percentile!'.format(test), voice='man')
    resp.say('Your openness is in the , {} percentile!'.format(test), voice='woman')
    resp.say('Your conscientiousness is in the , {} percentile!'.format(test), voice='alice')
    resp.say('Your extraversion is in the , {} percentile!'.format(test), voice='alice')
    resp.say('Your agreeableness is in the , {} percentile!'.format(test), voice='alice')


    resp.say('This is a test '.format(city), voice='alice')



    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)