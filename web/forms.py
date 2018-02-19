from django import forms


class FcmForm(forms.Form):
    title = forms.CharField(label='title')
    msg = forms.CharField(label='msg')