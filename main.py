import spotipy
from spotipy.oauth2 import SpotifyOAuth
import serial
import time

# api
SPOTIPY_CLIENT_ID = "YOUR_SPOTIPY_CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "YOUR_SPOTIPY_CLIENT_SECRET"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

# idk i got this from ai
scope = "user-read-currently-playing user-read-playback-state"

# auth the api
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

# port
ser = serial.Serial('COM7', 9600)
time.sleep(2)
def get_current_song():
    """Fetches the currently playing song from Spotify."""
    try:
        current_track = sp.current_playback()
        if current_track and current_track["is_playing"]:
            song_name = current_track["item"]["name"]
            artist_name = current_track["item"]["artists"][0]["name"]
            return f"{song_name}~{artist_name}"
        return "No Song Playing~"
    except Exception as e:
        print(f"Error: {e}")
        return "Error~"

while True:
    song_info = get_current_song()
    print(f"Now Playing: {song_info}")
    ser.write((song_info + "\n").encode('utf-8'))
    time.sleep(5)
