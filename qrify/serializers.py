from rest_framework import serializers
from .models import (
    UrlQrCode,TextQrCode,PhoneQrCode,EmailQRCode,
    VCardQRCode, EmailQRCode, SMSQRCode, WiFiQRCode, 
    SocialMediaQRCode, PdfQRCode, 
    MP3QRCode, AppStoreQRCode
)

class UrlQrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlQrCode
        fields = '__all__'

class TextQrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextQrCode
        fields = '__all__'
        
class PhoneQrCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneQrCode
        fields = '__all__'

class VCardQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VCardQRCode
        fields = '__all__'
class EmailQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailQRCode
        fields = '__all__'

class SMSQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSQRCode
        fields = '__all__'
        
class WiFiQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WiFiQRCode
        fields = '__all__'

class SocialMediaQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaQRCode
        fields = '__all__'
        
class PdfQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PdfQRCode
        fields = '__all__'
        
class MP3QRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MP3QRCode
        fields = '__all__'
class AppStoreQRCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppStoreQRCode
        fields = '__all__'
