Arduino-TFT-Spotify-Player

this project display the currently playing song from Spotify on a TFT LCD (MCUFRIEND) using an Arduino Uno (or Mega 2560) and a Python script that fetches song data via spotify api (Client ID and Client secret).

**Features:**
- Displays song title and artist on a the lcd.
- Updates every 5 seconds with new song data (you can change the time on the main.py line 40 time.sleep(x) ).
- Uses Python and Spotipy api to fetch real-time Spotify track info.
- Works on Arduino Uno & Arduino Mega.

Hardware & Software Requirements:
Required Hardware :
- Arduino Uno or Mega.
- MCUFRIEND 2.4" TFT LCD (Parallel connection).
- USB Cable.
- Computer running Python.

Required Software:
- Python 3 or above.

how to get spotify api Client ID and Client secret:
- visit : https://developer.spotify.com/dashboard
- Login to your spotify account.
- Create a new application.
- creat any app name and description.
- add the redirect link : http://localhost:8888/callback (make sure its matchs the SPOTIPY_REDIRECT_URI on main.py).
- Enable Web API Access.

some changes you need to change on main.py:
- please make sure to change the api.
SPOTIPY_CLIENT_ID = "your client id"
SPOTIPY_CLIENT_SECRET = "your client secret"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"

- and the port (line 21)
ser = serial.Serial('COM7', 9600)