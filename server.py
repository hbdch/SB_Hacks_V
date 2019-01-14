# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 23:57:42 2019

@author: Sahil
"""
from flask import Flask, request, render_template
from werkzeug import secure_filename
import personalityExtractor
import personalityComparison
import json
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client

app = Flask(__name__)
DEBUG = False
with open('config.json', 'r') as config_file:
    config_dict = json.load(config_file)
    account_sid = config_file["account_sid"]
    auth_token = config_file["auth_token"]

client = Client(account_sid, auth_token)


@app.route('/', methods=['GET'])
def display():
    return render_template('index.html')

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        if DEBUG:
            print(request.files)
            
        if 'myfile' not in request.files and DEBUG:
            print("File does not exist")
        f = request.files['myfile']
        f.save(secure_filename(f.filename))

        # The dictionary of traits is called values.json within the data folder
        # The list of the top 5 companies is called results.json within the data folder
        text = personalityExtractor.loadText(f.filename)
        profile = personalityExtractor.getPersonalityTraits(text)
        personalityTraits = personalityExtractor.findTraits(profile["personality"])

        companies = personalityComparison.loadJSONData("data/company_data.json")
        results = personalityComparison.compareData(personalityTraits, companies)
        personalityComparison.saveResults(results)

        return render_template('pagetwo.html')
    else:
        return render_template('index.html')

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls and mention the caller's city"""
    # After this, you have to read the .json files to access results :)
    with open('data/values.json') as values:
        candidate_profile = json.load(values)

    with open('data/results.json') as result:
        companies = json.load(result)

    # Start our TwiML response
    resp = VoiceResponse()

    resp.say('Your results are in.', voice='man')
    # Read a message aloud to the caller
    for key in candidate_profile:
        percent = candidate_profile[key] * 100
        percent = round(percent, 2)
        resp.say(f"Your {key} is in the {percent}th percentile!", voice='man')

    resp.say(f"You matched with {companies[0]}", voice='man')
    for index in range(1, len(companies)):
        resp.say(f" {companies[index]}", voice='man')

    return str(resp)

@app.route("/phone", methods=['POST'])
def make_call():
    number = request.form['the_phone']
    number = '+1' + number
    
    call = client.calls.create(
            url='https://267c0346.ngrok.io/voice',
            to=number,
            from_='+18315080310'
        )
    return render_template('pagetwo.html')


if __name__ == "__main__":
    app.run()
