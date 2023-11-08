from django import forms
from .models import UrlQrCode, TextQrCode

class UrlQrCodeForm(forms.ModelForm):
    class Meta:
        model = UrlQrCode
        fields = ['url']  

class TextQrCodeForm(forms.ModelForm):
    class Meta:
        model = TextQrCode
        fields = ['text'] 
