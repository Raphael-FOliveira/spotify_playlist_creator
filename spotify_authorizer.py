import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URI = "http://example.com"
scope = "playlist-modify-public"
user_id = os.environ["SPOTIFY_USER_ID"]
auth_manager = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=scope)
token = auth_manager.get_access_token()

spotify = spotipy.Spotify(client_credentials_manager=auth_manager)
