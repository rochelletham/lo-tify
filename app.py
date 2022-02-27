import re
from flask import Flask, redirect, render_template, request, jsonify, url_for
import os
import requests
from pydub import AudioSegment

from secret import *

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth


# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=lotify_client,
#                                                client_secret=lotify_client_secret,
#                                                redirect_uri=redirect_uri,
#                                                scope="user-library-read"))

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
  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=lotify_client,
                                               client_secret=lotify_client_secret,
                                               redirect_uri=redirect_uri,
                                               scope="user-library-read"))
  results = sp.current_user_top_tracks(limit=5, time_range="long_term")
  for idx, item in enumerate(results['items']):
      track = item['track']
      print(idx, track['artists'][0]['name'], " - ", track['name'])

      # Spotify returns .mp3 preview
      mp3_preview = requests.get(track['preview_url'])
      with open(f"audio/{track['name']}.mp3", "wb") as fd:
        fd.write(mp3_preview.content)
      
      # convert .mp3 to .wav
      sound = AudioSegment.from_file(f"audio/{track['name']}.mp3")
      sound.export(f"audio/{track['name']}.wav")
      os.remove(f"audio/{track['name']}.mp3")

  return "YAY", 200

# @app.route('/callback')
# def callback():
  return render_template("spotify_login_callback.html")

@app.route('/spotify', methods=["POST"])
def POST_spotify():
  # spotify API call 
  server_url = os.getenv('SPOTIFY_URL')
  spotify = requests.get(f'{server_url} ..... ')  
  if (spotify is None):
    return f"No data available", 404
  
  spotify_data = spotify.json()

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)