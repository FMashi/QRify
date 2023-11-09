
from django.contrib import admin

from .models import (
    UrlQrCode,TextQrCode,PhoneQrCode,EmailQRCode,
    VCardQRCode, EmailQRCode, SMSQRCode, WiFiQRCode, 
    SocialMediaQRCode, PdfQRCode, 
    MP3QRCode, AppStoreQRCode
)
@admin.register(UrlQrCode)
class UrlQrCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'url')
    list_filter = ('url',) 
    search_fields = ('url',)

@admin.register(TextQrCode)
class TextQrCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_filter = ('text',) 
    search_fields = ('text',)  

@admin.register(PhoneQrCode)
class PhoneQrCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'number')
    list_filter = ('number',) 
    search_fields = ('number',)  


@admin.register(VCardQRCode)
class VCardQRCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'company', 'city', 'state', 'country')
    list_filter = ('city', 'state', 'country')
    search_fields = ('name', 'email')

@admin.register(EmailQRCode)
class EmailQRCodeAdmin(admin.ModelAdmin):
    list_display = ('email',)
    search_fields = ('email',)

@admin.register(SMSQRCode)
class SMSQRCodeAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_filter = ('number',)
    search_fields = ('number',)

@admin.register(WiFiQRCode)
class WiFiQRCodeAdmin(admin.ModelAdmin):
    list_display = ('ssid', 'encryption', 'hidden')
    list_filter = ('encryption', 'hidden')
    search_fields = ('ssid',)


@admin.register(SocialMediaQRCode)
class SocialMediaQRCodeAdmin(admin.ModelAdmin):
    list_display = ('type', 'profile', 'post', 'username')
    list_filter = ('type',)
    search_fields = ('profile', 'username')

@admin.register(PdfQRCode)
class PdfQRCodeAdmin(admin.ModelAdmin):
    list_display = ('pdf_file',)
    search_fields = ('pdf_file',)

@admin.register(MP3QRCode)
class MP3QRCodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'audio_file')
    search_fields = ('title', 'artist')

@admin.register(AppStoreQRCode)
class AppStoreQRCodeAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'platform', 'app_url')
    list_filter = ('platform',)
    search_fields = ('app_name', 'platform')

  
