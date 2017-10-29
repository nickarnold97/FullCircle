import sys
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
	return render_template('main.html')

app.run(host = '0.0.0.0',port = 3333, debug = True)