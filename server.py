# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 23:57:42 2019

@author: Sahil
"""
from flask import Flask, request, render_template
from werkzeug import secure_filename

app = Flask(__name__)
DEBUG = False
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
        return render_template('received.html', fname=f.filename)
    else:
        return render_template('index.html')
        

def call_api():
    pass

if __name__ == "__main__":
    app.run()
