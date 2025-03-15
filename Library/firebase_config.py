import pyrebase
import json

with open("firebase_credentials.json") as f:
    config = json.load(f)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()