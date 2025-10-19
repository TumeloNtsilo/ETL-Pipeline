import requests
import pandas as pd

def artistName():
    """Takes the artist's name from the user.
    Returns that artist's name."""
    artist_name = ""
    while not artist_name or artist_name == "":
        artist_name = input("Please enter the artist's name: ")
    return artist_name

def extract(artist_name):
    """Extract 100 songs using an artist's name from the iTunes API
    Returns the results as a DataFrame."""

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

def transform(df):
    """Transforms the DataFrame an rearranges it in order.
    Renames some of the headings of the DataFrame"""

    df = df[["artistName", "trackName", "collectionName", "primaryGenreName", "releaseDate", "trackPrice", "collectionPrice", "currency", "trackExplicitness", "isStreamable"]]
    df = df.rename(columns={
        "collectionName": "album",
        "collectionPrice": "album_price",
        "trackPrice": "song_price",
        "trackName": "song_title",
        "trackExplicitness": "explicit",
        "primaryGenreName": "genre"
    })

    return df


def load(df, artist_name, delimiter):
    """Load transformed data into a CSV file."""
    filename = f"{artist_name}_songs.csv"
    try:
        df.to_csv(filename, sep=delimiter)
        return "Successfully loaded the data to csv."
    except:
        return "Error, data was not successfully loaded into the csv."
    
def main():
    """Runs the full ETL pipeline for a given artist."""
    artist_name = artistName()
    df = extract(artist_name)

    if df is not None:
        transformedData = transform(df)
        load(transformedData, artist_name, ",")
        return f"iTunes ETL pipeline ran succesfully for {artist_name}"
    else:
        return "Extraction failed. Please try again."
    
if __name__ == "__main__":
    print(main())
