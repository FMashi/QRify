
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html, mark_safe
from .models import (
    UrlQrCode,TextQrCode,PhoneQrCode,EmailQRCode,
    VCardQRCode, EmailQRCode, SMSQRCode, WiFiQRCode, 
    SocialMediaQRCode, PdfQRCode, 
    MP3QRCode, AppStoreQRCode
)
class QRCodeBaseAdmin(admin.ModelAdmin):
    list_display = ('display_thumbnail',)

    def display_thumbnail(self, obj):
        if obj.image:
            return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        return None

    display_thumbnail.short_description = 'QR Code'

@admin.register(UrlQrCode)
class UrlQrCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'url','display_thumbnail')
    list_filter = ('url',) 
    search_fields = ('url',)
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)
    
@admin.register(TextQrCode)
class TextQrCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'text','display_thumbnail')
    list_filter = ('text',) 
    search_fields = ('text',)  
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)

@admin.register(PhoneQrCode)
class PhoneQrCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'number','display_thumbnail')
    list_filter = ('number',) 
    search_fields = ('number',)  
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)


@admin.register(VCardQRCode)
class VCardQRCodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'company', 'city', 'state', 'country','display_thumbnail')
    list_filter = ('city', 'state', 'country')
    search_fields = ('name', 'email')
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)

@admin.register(EmailQRCode)
class EmailQRCodeAdmin(admin.ModelAdmin):
    list_display = ('email','display_thumbnail')
    search_fields = ('email',)
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)

@admin.register(SMSQRCode)
class SMSQRCodeAdmin(admin.ModelAdmin):
    list_display = ('number','display_thumbnail')
    list_filter = ('number',)
    search_fields = ('number',)
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)

@admin.register(WiFiQRCode)
class WiFiQRCodeAdmin(admin.ModelAdmin):
    list_display = ('ssid', 'encryption', 'hidden','display_thumbnail')
    list_filter = ('encryption', 'hidden')
    search_fields = ('ssid',)
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)


@admin.register(SocialMediaQRCode)
class SocialMediaQRCodeAdmin(admin.ModelAdmin):
    list_display = ('type', 'profile', 'post', 'username','display_thumbnail')
    list_filter = ('type',)
    search_fields = ('profile', 'username')
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)

@admin.register(PdfQRCode)
class PdfQRCodeAdmin(admin.ModelAdmin):
    list_display = ('pdf_file','display_thumbnail')
    search_fields = ('pdf_file',)
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)

@admin.register(MP3QRCode)
class MP3QRCodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'audio_file','display_thumbnail')
    search_fields = ('title', 'artist')
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)

@admin.register(AppStoreQRCode)
class AppStoreQRCodeAdmin(admin.ModelAdmin):
    list_display = ('app_name', 'platform', 'app_url','display_thumbnail')
    list_filter = ('platform',)
    search_fields = ('app_name', 'platform')
    
    def display_thumbnail(self, obj):
        return QRCodeBaseAdmin.display_thumbnail(self, obj)

  
