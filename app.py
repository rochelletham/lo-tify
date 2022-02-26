import re
from flask import Flask, redirect, render_template, request, jsonify, url_for
import os
from flask.scaffold import F
import requests

from secret import *

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# generic call 
# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=lotify_client,
#                                                            client_secret=lotify_client_secret))

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=lotify_client,
                                               client_secret=lotify_client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read"))

app = Flask(__name__)
# Route for "/" (frontend):
@app.route('/')
def index():
  return render_template("index.html")
 
@app.route('/login.html')
def login():
  return render_template("login.html")

@app.route('/spotify_login')
def spotify_login():
  results = sp.current_user_saved_tracks()
  for idx, item in enumerate(results['items']):
      track = item['track']
      print(idx, track['artists'][0]['name'], " – ", track['name'])
  return "YAY", 200

@app.route('/callback')
def callback():
  return render_template("spotify_login_callback.html")

@app.route('/spotify', methods=["POST"])
def POST_spotify():
  # spotify API call 
  server_url = os.getenv('SPOTIFY_URL')
  spotify = requests.get(f'{server_url} ..... ')  
  if (spotify is None):
    return f"No data available", 404
  
  spotify_data = spotify.json()   
