# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
from gevent.pywsgi import WSGIServer
import numpy as np
import re
import requests
import os 

app = Flask(__name__)

def check(output):

    url = "https://image-to-text2.p.rapidapi.com/cloudVision/imageToText"
    
    querystring = {"source":output,"sourceType":"url"}
    
    payload = '''{\r\n    \"source\": "'''+output+'''" ,\r\n    \"sourceType\": \"url\"\r\n}'''
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "c6135028f7msh4c1cda7b60c7f78p10c530jsnfef136b11722",
        'x-rapidapi-host': "image-to-text2.p.rapidapi.com"
        }
    
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    
    print(response.text)
    return (response.json()['text'])
    

#home page
@app.route('/')
def home():
    return render_template('base.html')

#Summarizer page
@app.route('/predict',methods=['POST'])
def predict():
    output=request.form['output']
    text=check(output)
    return render_template('base.html',output=text)

port = os.getenv('VCAP_APP_PORT', '8080')
    
if __name__ == "__main__":
    app.secret_key= os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=port)