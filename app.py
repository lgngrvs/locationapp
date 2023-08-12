from flask import Flask, request, jsonify, send_from_directory
import requests

import firebase_admin
from firebase_admin import auth, credentials

app = Flask(__name__)

GOOGLE_VERIFY_URL = "https://www.googleapis.com/oauth2/v3/tokeninfo"
CLIENT_ID = "locationservice-16ebc.apps.googleusercontent.com"
cred = credentials.Certificate("credentials/adminsdk.json")
firebase_admin.initialize_app(cred)


@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


@app.route('/verify', methods=['POST'])
def verify_token():
    id_token = request.json.get('id_token')
    
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return jsonify(success=True, message="Token is valid")
    except:
        return jsonify(success=False, message="Token verification failed")

if __name__ == "__main__":
    app.run(debug=True)
