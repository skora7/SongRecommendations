import requests

# Important constants such as  Developer ID, secret code, and API URL
CLIENT_ID = '9f70274296174bcbb7433c0f52a936cf'
CLIENT_SECRET = '001c169fadf84870811538da8ac3b06d'
BASE_URL = 'https://api.spotify.com/v1'



# Acquire access token
auth_response = requests.post('https://accounts.spotify.com/api/token', {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']



# Save default "headers" parameter
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}







# Example of getting the audio features of a track
track_id = '6y0igZArWVi6Iz0rj35c1Y'

r = requests.get(BASE_URL + '/audio-features/' + track_id, headers=headers)

r = r.json()
print(r)
print()



# Example of getting all available seed genres
r = requests.get(BASE_URL + '/recommendations/available-genre-seeds', headers=headers)

r = r.json()
print(r)
print()



# Example of getting genres associated with an artist (Dot Demo)
artist_id = '2ID5ZEW2EbdUo1oEjwJnD3'

r = requests.get(BASE_URL + '/artists/' + artist_id, headers=headers)

r = r.json()
print("Dot Demo Genres:")
print(r['genres'])
print()



# Example of getting genres associated with an artist (Travis Scott)
artist_id = '0Y5tJX1MQlPlqiwlOH1tJY'

r = requests.get(BASE_URL + '/artists/' + artist_id, headers=headers)

r = r.json()
print("Travis Scott Genres:")
print(r['genres'])
print()