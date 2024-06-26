# SpotiFynd Data CLI
A command-line interface (CLI) using Typer for a user’s Spotify statistics. Given a command, the program will send a Spotify Web API request using the Spotipy library, which will return the requested information (such as an artist’s top N tracks, the most popular tracks in the US right now, tempo of a song, etc.)

There are many Spotify command-line apps (For instance, Spotify-cli), but most have more of a focus on being an interface (playback, creating playlists, etc.) than a data tool. Rather than being an alternative frontend/UI to the Spotify desktop app, this application focuses more on quickly and easily accessing song data (which isn’t available in the desktop app).

Proof of feasibility: https://github.com/tuo20482/spotify-data-cli

## Prerequisites
- Python 3.8 or higher
- A Spotify Developer account to provide your own Client ID and Client Secret for accessing the Spotify Web API


## Installation
1. Clone this repository to your local machine.
2. Navigate to the cloned directory.
3. Create a virtual environment:

**Note: For users with later versions of python. The python and pip commands have been updataed to python3 & pip3.
If this is the case on your machine, then replace python and pip keywords with python3 and pip3 respectively.**
```
python -m venv venv
```
4. Activate the virtual environment:
- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```
5. Install the required dependencies:
```
pip install -r requirements.txt
```

## Login & Authentication
The first time running any command will prompt the user to login to their Spotify account and allow SpotiFynd application access.

If this process fails or returns an error, it is likely due to an incompatible .cache file from a previous iteration. Delete the .cache file and attempt running a command again.


## Running the Application & Requirements
- Running the program always requires a mode.
- There are 4 modes when running the applications: _search_, _top-tracks_, _suggest_ & _create-playlist_. Each of which has different running requirements.

**Mode Descriptions**
- search: Users receive suggested tracks and their song features based on input artist or song name(s) and flagged features.
- top-tracks: Users receive songs that fit within their specified artist/song name and the flagged features. Used to retrieve tracks with specific information.
- suggest: Users receive up to 100 suggested songs based on their saved songs, listening history, and most listened to genres.
- playlist: Creates a playlist on the users spotify account with the songs from the most previously generated list of songs. Requires songs to be output before running.

**Mode Requirements and Examples**

- Format:
  ```
  python main.py mode --required_flags --optional_flags
  ```

**Search**
- Required Flags: A minimum of at least one flag of artist, genre, and/or song flags. The amount of input values following these flags cannot exceed 5 items.
- Optional Flags: Any number of song feature flags (bottom of document) to filter the songs by.

- Example:
  ```
  python main.py search  -a "Kendrick Lamar, Dolly Parton" -s "Dancing Queen, Bohemian Rhapsody" -g "Reggae" -t "100-200"
  ```

**top-tracks**
- Required Flags: One of either artist or song flag.
- Optional Flags: Any number of song feature flags.

- Example:
  ```
  python main.py top-tracks -s "Dancing Queen" -ac "0.2-0.6" -ts "4"
  ```

**suggest**
- Required Flags: None
- Optional Flags: --limit: Limits the number of songs returned to the user, up to a maximum of 100.

- Example:
  ```
  python main.py suggest --limit 100
  ```
  
**playlist**
- Required Flags: -n: Name of the playlist that will be generated.
- Optional Flags: None

- Example:
  ```
  python main.py playlist -n "My Playlist Name" 


## Song Feature Flags Dictionary

- Artist: '-a'  or '--artist'
 Song: '-s'  or '--song'
- Pitch: '-p'  or '--pitch'
- Tempo: '-t'  or '--tempo'
- Danceability: '-d'  or '--dance'
- Acousticness: '-ac' or '--acoust' for acoustic"
- Time Signature: '-ts' or '--time_signature'
- Liveness: '-l'  or '--liveness'
- Energy: '-e'  or '--energy'
- Speechiness:'-sp' or '--speechiness'
