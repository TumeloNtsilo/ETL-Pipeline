import requests
import pandas as pd

def extract(artist_name):
    """Extract 100 songs using an artist's name from the iTunes API"""
    url = f"https://itunes.apple.com/search?term={artist_name}&entity=song"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        songs = data["results"]

        df = pd.DataFrame(songs)

        return df
    else:
        print("Error! Something went wrong: " + str(response.status_code))
        return None

def transform():
    pass

def load():
    pass
