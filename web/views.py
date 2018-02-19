import firebase_admin
from django.shortcuts import render

# Create your views here.
from firebase_admin import credentials, db


def index(request):
    cred = credentials.Certificate('service_key.json')
    try:
        app = firebase_admin.get_app()
    except ValueError:
        app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://kagandroidapp.firebaseio.com/'})

    return render(request, 'index.html')
