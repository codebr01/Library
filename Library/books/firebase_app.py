# books/firebase_app.py
import firebase_admin
from firebase_admin import credentials
from django.conf import settings

if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS)
    firebase_admin.initialize_app(cred, {
        'databaseURL': settings.FIREBASE_DATABASE_URL
    })