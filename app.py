import re
from flask import Flask, render_template, request, jsonify
import os
from flask.scaffold import F
import requests

app = Flask(__name__)

# Route for "/" (frontend):
@app.route('/')
def index():
  return render_template("index.html")
 
@app.route('/spotify', methods=["POST"])
def POST_spotify():
  # spotify API call 
  server_url = os.getenv('SPOTIFY_URL')
  spotify = requests.get(f'{server_url} ..... ')  
  if (spotify is None):
    return f"No data available", 404
  
  spotify_data = spotify.json()   
