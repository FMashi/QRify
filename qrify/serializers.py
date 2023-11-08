from rest_framework import serializers
from .models import UrlQrCode, TextQrCode

class UrlQrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlQrCode
        fields = '__all__'

class TextQrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQrCode
        fields = '__all__'
