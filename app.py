import requests
import secrets
from flask import Flask, redirect, request, session, url_for

app = Flask(__name__)  # Fix: change _name_ to __name__
app.secret_key = 'your_secret_key'

AUTH_SERVER = 'http://example.com'  # Replace with your actual auth server
CLIENT_ID = 'Ov23li9t48jyAZvywfAd'  # Replace with your actual client ID
CLIENT_SECRET = '20658b4462564fba31c870b2011e36f1073fd051'  # Replace with your actual client secret
REDIRECT_URI = 'http://localhost:8000/callback'  # Updated to use port 8000
SCOPE = 'read_profile'
STATE = secrets.token_urlsafe(16)
NONCE = secrets.token_urlsafe(16)

@app.route('/login')
def login():
    auth_url = f"{AUTH_SERVER}/authorize?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={SCOPE}&state={STATE}&nonce={NONCE}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')

    if state != STATE:
        return "Invalid state parameter", 400

    token_url = f"{AUTH_SERVER}/token"
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(token_url, data=token_data)
    token_response = response.json()

    session['access_token'] = token_response['access_token']
    return "Login successful"

@app.route('/profile')
def profile():
    access_token = session.get('access_token')

    if not access_token:
        return redirect(url_for('login'))

    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(f"{AUTH_SERVER}/profile", headers=headers)
    profile_data = response.json()

    return profile_data

if __name__ == '__main__':
    app.run(port=8000)  # Changed to use port 8000 and removed SSL context

