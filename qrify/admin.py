
from django.contrib import admin
from .models import UrlQrCode, TextQrCode

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
