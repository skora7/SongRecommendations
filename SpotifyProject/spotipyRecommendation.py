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
