import requests

#Daniel's developer ID and secret code to connect to api
CLIENT_ID = '9f70274296174bcbb7433c0f52a936cf'
CLIENT_SECRET = '001c169fadf84870811538da8ac3b06d'

#send post request to spotify api to create token
auth_response = requests.post('https://accounts.spotify.com/api/token', {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']
