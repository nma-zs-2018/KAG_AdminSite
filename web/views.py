import firebase_admin
from django.shortcuts import render

# Create your views here.
from firebase_admin import credentials, db


def index(request):
    cred = credentials.Certificate('web/serviceKey.json')
    try:
        app = firebase_admin.get_app()
    except ValueError:
        app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://sandbox-c9049.firebaseio.com/'})
    ref = db.reference('/test', app)
    json = ref.get()
    return render(request, 'index.html', {'name': json})
