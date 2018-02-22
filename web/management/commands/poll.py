import firebase_admin
from django.core.management import BaseCommand
import requests
from firebase_admin import credentials, messaging
import json

from web.models import PollData


class Command(BaseCommand):

    def handle(self, *args, **options):
        resp = requests.get('http://azuolynogimnazija.lt/json/svarbu', headers={'User-Agent': ''})
        data = json.loads(resp.text)
        last = PollData.objects.get(id='alert')
        if not last:
            obj = PollData()
            obj.timestamp = data['updated_at']
            obj.id = data['alert']
            obj.save()
        elif last.timestamp == data['updated_at']:
            return

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
