import firebase_admin
from django.core.management import BaseCommand
import requests
from firebase_admin import credentials, messaging
import json

headers = {'User-Agent': ''}


class Command(BaseCommand):

    def handle(self, *args, **options):
        resp = requests.get('http://azuolynogimnazija.lt/json/svarbu', headers=headers)
        print(resp.text)
        data = json.loads(resp.text)
        cred = credentials.Certificate('service_key.json')

        try:
            app = firebase_admin.get_app()
        except ValueError:
            app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://kagandroidapp.firebaseio.com/'})

        message = messaging.Message(
            notification=messaging.Notification(
                title=data['title'],
                body=data['text']
            ),
            android=messaging.AndroidConfig(
                restricted_package_name='com.simaskuprelis.kag_androidapp.dev'
            ),
            topic='test'
        )

        messaging.send(message, app=app)
