import firebase_admin
from django.shortcuts import render

# Create your views here.
from firebase_admin import credentials, messaging

from web.forms import FcmForm


def index(request):
    cred = credentials.Certificate('service_key.json')
    try:
        app = firebase_admin.get_app()
    except ValueError:
        app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://kagandroidapp.firebaseio.com/'})

    if request.method == 'POST':
        form = FcmForm(request.POST)
        if form.is_valid():
            message = messaging.Message(
                notification=messaging.Notification(
                    title=form.cleaned_data['title'],
                    body=form.cleaned_data['msg']
                ),
                android=messaging.AndroidConfig(
                    restricted_package_name='com.simaskuprelis.kag_androidapp.dev'
                ),
                topic='test'
            )
            print(messaging.send(message, app=app))
    else:
        form = FcmForm()

    return render(request, 'index.html', {'form': form})
