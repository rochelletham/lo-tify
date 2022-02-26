import re
from flask import Flask, render_template, request, jsonify
import os
from flask.scaffold import F
import requests

from secret import *

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=lotify_client,
                                                           client_secret=lotify_client_secret))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

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
