import unittest
from itunes_etl import*
import os

class TestsiTunesETL(unittest.TestCase):
    def test_extract_returns_dataframe(self):
        self.assertIsInstance(extract("Drake"), pd.DataFrame)
        self.assertGreater(len(extract("Drake")), 0)

    def test_transform_columns(self):
        data = {
            "artistName": ["A-Reece"],
            "trackName": ["Song 1"],
            "collectionName": ["Album 1"],
            "primaryGenreName": ["Hip-Hop"],
            "releaseDate": ["2023-01-01"],
            "trackPrice": [1.29],
            "collectionPrice": [9.99],
            "currency": ["USD"],
            "trackExplicitness": ["explicit"],
            "isStreamable": [True]
        }
        df = pd.DataFrame(data)
        transformed = transform(df)

        expected_columns = ["artistName", "song_title", "album", "genre",
                            "releaseDate", "song_price", "album_price", "currency", "explicit", "isStreamable"]
        self.assertEqual(list(transformed.columns), expected_columns)

    def test_load_creates_file(self):
        data = {
            "artistName": ["A-Reece"],
            "song_title": ["Song 1"],
            "album": ["Album 1"],
            "genre": ["Hip-Hop"],
            "releaseDate": ["2023-01-01"],
            "song_price": [1.29],
            "album_price": [9.99],
            "currency": ["USD"],
            "explicit": ["explicit"],
            "isStreamable": [True]
        }
        df = pd.DataFrame(data)
        filename = "test_output.csv"

        load(df, "test_artist", ",")
        
        self.assertTrue(os.path.isfile("test_artist_songs.csv"))
        
        os.remove("test_artist_songs.csv")

if __name__ == "__main__":
    unittest.main()