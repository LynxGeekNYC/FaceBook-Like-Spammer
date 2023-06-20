import requests

# Set up your access token and the username you want to convert to user ID
access_token = 'YOUR_ACCESS_TOKEN'
username = 'username'

# API endpoint to convert username to user ID
endpoint = f'https://graph.facebook.com/{username}'

# Parameters to include access token
params = {
    'access_token': access_token
}

# Send a GET request to the API endpoint
response = requests.get(endpoint, params=params)

# Process the response
if response.status_code == 200:
    data = response.json()
    user_id = data['id']
    print(f"User ID for '{username}': {user_id}")
else:
    print('Failed to retrieve user ID:', response.json())
