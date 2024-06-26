from pkce import spotify
import pandas as pd

def create_playlist(name: str = "test-playlist", is_public: bool = True) -> str:
    return spotify.user_playlist_create(user=spotify.current_user()["id"], name=name, public=is_public)["id"]

def get_playlists_info() -> pd.DataFrame:
    results = spotify.current_user_playlists(limit=10, offset=0)
    playlist_name = []
    playlist_id = []
    playlist_public = []
    playlist_tracks = []
    for item in results["items"]:
        playlist_name.append(item["name"])
        playlist_id.append(item["id"])
        playlist_public.append(item["public"])
        playlist_tracks.append(item["tracks"])

    # Create the final df   
    df = pd.DataFrame({ "playlist_name": playlist_name, 
                                "playlist_id": playlist_id, 
                                "playlist_public": playlist_public,
                                "playlist_tracks":playlist_tracks})

    return df

def add_to_playlist(playlist_id: str, position: int = 0):
    songs = [uri for song, uri in pd.read_html("df.html", encoding="utf-8", extract_links="body")[0]["Song"]]
    spotify.playlist_add_items(playlist_id, songs, position)
