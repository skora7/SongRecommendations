import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Important constants such as  Developer ID, secret code, and API URL
CLIENT_ID = '9f70274296174bcbb7433c0f52a936cf'
CLIENT_SECRET = '001c169fadf84870811538da8ac3b06d'

# Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

sp.audio_features('3GCdLUSnKSMJhs4Tj6CV3s') [0]

print(sp.audio_features('3GCdLUSnKSMJhs4Tj6CV3s'))

# Data Selection Deleting Duplicate Songs in Playlists
def drop_duplicates(df):
    """
    Drop Duplicate Songs
    :param df: Collect artist name and track titles
    :return: Delete replicated songs
    """
    df['3GCdLUSnKSMJhs4Tj6CV3s'] = df.apply(lambda row: row['artist_name'] + row['3GCdLUSnKSMJhs4Tj6CV3s'], axis=1)
    return df.drop_duplicates('3GCdLUSnKSMJhs4Tj6CV3s')


songDF = drop_duplicates(playlistDF)

# Select Only Useful Columns
def select_cols(df):
    """
    Select Only Useful Columns
    :param df: Use only relevant features
    :return: Return relevant features
    """
    return df[['artist_name', 'id', 'track_name', 'danceability', 'energy', 'key', 'loudness', 'mode',
           'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', "artist_pop",
           "genres", "track_pop"]]


songDF = select_cols(songDF)
songDF.head()

# List Concatenation
def genre_preprocess(df):
    """
    Preprocess Genre Data
    :param df: Convert genre columns back to a list
    :return: list
    """
    df['genre_list'] = df['genres'].apply(lambda x: x.split(" "))
    return df


songDF = genre_preprocess(songDF)
songDF['genre_list'].head()

# Convert data into Metadata
def ohe_prep(df, column, new_name):
   """
   Create One Hot Encoded features of a specific column
   :param df: (pandas dataframe): Spotify Dataframe
   :param column: (str): Column to be processed
   :param new_name: (str): New column to be used
   :return: One-hot encoded features
   """
    tf_df = pd.get_dummies(df[column])
    feature_names = tf_df.columns
    tf_df.columns = [new_name + "|" + str(i) for i in feature_names]
    tf_df.reset_index(drop = True, inplace = True)
    return tf_df

"""
# Term Frequency - Inverse Document Frequency Implementation
tfidf = Tfidfvectorizer()
tfidf_matrix = tfidf.fit_transform(songDF['genres_list'].apply(lambda x: " ".join(x)))
genre_df = pd.DataFrame(tfidf_matrix.toarray())
genre_df.columns = ['genre' + "|" + i for i in tfidf.get_feature_names()]
genre_df.drop(columns='genre|unknown')
genre_df.reset_index(drop = True, inplace=True)
genre_df.iloc[0]

# Normalization
pop =  songDF[["artist_pop"]].reset_index(drop = True)
scaler = MinMaxScaler()
pop_scaled = pd.DataFrame(scaler.fit_transform(pop), columns = pop.columns)
pop_scaled.head()

# One-hot Encoding
key_ohe = ohe_prep(df, 'key', 'key') * 0.5
mode_ohe = ohe_prep(df, 'mode', 'mode') * 0.5

# Scale audio columns
floats = df[float_cols].reset_index(drop = True)
scaler = MinMaxScaler()
floats_scaled = pd.DataFrame(scaler.fit_transform(floats), columns = floats.columns) * 0.2
"""

