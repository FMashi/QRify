import os
from django.utils import timezone
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image,ImageDraw, ImageFont
from ckeditor.fields import RichTextField
import uuid 
from django.utils.html import strip_tags,escape
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

def qr_code_upload_path(instance, filename):
    folder_name = timezone.now().strftime('%Y/%m/%d')
    if isinstance(instance, UrlQrCode):
        subfolder_name = 'url'
    elif isinstance(instance, TextQrCode):
        subfolder_name = 'text'
    elif isinstance(instance, PhoneQrCode):
        subfolder_name = 'phone'
    elif isinstance(instance, VCardQRCode):
        subfolder_name = 'vcard'
    elif isinstance(instance, EmailQRCode):
        subfolder_name = 'email'
    elif isinstance(instance, SMSQRCode):
        subfolder_name = 'sms'
    elif isinstance(instance, WiFiQRCode):
        subfolder_name = 'wifi'
    elif isinstance(instance, SocialMediaQRCode):
        subfolder_name = 'media'
    elif isinstance(instance, PdfQRCode):
        subfolder_name = 'pdf'
    elif isinstance(instance, MP3QRCode):
        subfolder_name = 'mp3'
    elif isinstance(instance, AppStoreQRCode):
        subfolder_name = 'app'
    else:
        subfolder_name = 'other'
        
    upload_path = os.path.join('qr-codes/', subfolder_name, folder_name)
    return os.path.join(upload_path, filename)

class QRCodeBase(models.Model):
    image = models.ImageField(upload_to=qr_code_upload_path, blank=True, verbose_name='QR Code Image')

    class Meta:
        abstract = True

    def generate_unique_filename(self):
        unique_id = str(uuid.uuid4())
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        return f"{timestamp}_{unique_id}.png"

    def generate_qr_code(self, content):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(content)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        qr_code_image = File(buffer, name=self.generate_unique_filename())

        self.image.save(self.generate_unique_filename(), qr_code_image, save=False)

    def save(self, *args, **kwargs):
        if not self.image:
            self.generate_qr_code(self.get_qr_code_content())
        super().save(*args, **kwargs)

class UrlQrCode(QRCodeBase):
    url = models.URLField(blank=True, null=True, verbose_name='URL')
    
    class Meta:
        verbose_name = ("Url QrCode")
        verbose_name_plural = ("Url")

    def __str__(self):
        return self.url

    def get_qr_code_content(self):
        return self.url
    
    def get_absolute_url(self):
        return reverse('qr_code_detail', args=[str(self.id)])

class TextQrCode(QRCodeBase):
    text = RichTextField(blank=True,max_length=500, null=True, verbose_name='Text Content')
    class Meta:
        verbose_name = ("Text QrCode")
        verbose_name_plural = ("Text")

    def __str__(self):
        return strip_tags(self.text)

    def get_qr_code_content(self):
        plain_text = strip_tags(self.text)
        return escape(plain_text)
    
    def get_absolute_url(self):
        return reverse('qr_code_detail', args=[str(self.id)])

class PhoneQrCode(QRCodeBase):
    number = PhoneNumberField(blank=True, null=True, verbose_name='Phone Number')
    class Meta:
        verbose_name = ("Phone QrCode")
        verbose_name_plural = ("Phone")

    def __str__(self):
        return str(self.number)

    def get_qr_code_content(self):
        return str(self.number)
    
    def get_absolute_url(self):
        return reverse('phone_qr_code_detail', args=[str(self.id)])
    
class VCardQRCode(QRCodeBase):
    name = models.CharField(max_length=150)
    contact = PhoneNumberField(blank=True, null=True,verbose_name='Phone Number')
    email = models.EmailField(max_length=255)
    company = models.CharField(blank=True, null=True,max_length=150)
    street = models.CharField(blank=True, null=True,max_length=100)
    city = models.CharField(blank=True, null=True,max_length=100)
    state = models.CharField(blank=True, null=True,max_length=100)
    country = models.CharField(blank=True, null=True,max_length=100)
    website = models.URLField(blank=True, null=True,max_length=255)
    
    class Meta:
        verbose_name = "V Card QR Code"
        verbose_name_plural = "VCard"

    def __str__(self):
        return self.name

    def get_qr_code_content(self):
        vcard_content = f"BEGIN:VCARD\n" \
                       f"VERSION:3.0\n" \
                       f"N:{self.name}\n" \
                       f"FN:{self.name}\n" \
                       f"ORG:{self.company}\n" \
                       f"TITLE:{self.contact}\n" \
                       f"TEL:{self.contact}\n"\
                       f"EMAIL:{self.email}\n" \
                       f"ADR:;;{self.street};{self.city};{self.state};{self.country}\n" \
                       f"URL:{self.website}\n" \
                       f"END:VCARD"
        return vcard_content
    
class EmailQRCode(QRCodeBase):
    email = models.EmailField(max_length=255)
    
    class Meta:
        verbose_name = "Email QR Code"
        verbose_name_plural = "Email"
        
    def __str__(self):
        return self.email
    
    def get_qr_code_content(self):
        return f"mailto:{self.email}"

class SMSQRCode(QRCodeBase):
    number = PhoneNumberField(max_length=20, verbose_name='Phone Number')
    # message = models.TextField(verbose_name='SMS Message')
    class Meta:
        verbose_name = "SMS QR Code"
        verbose_name_plural = "SMS"
    
    def get_qr_code_content(self):
        sms_content = f'sms:{self.number}'
        # sms_content = f'sms:{self.number}?&body={self.message}'
        return sms_content
    def __str__(self):
        return f'SMS QR Code: {self.number}'

    def get_absolute_url(self):
        return reverse('sms_qr_code_detail', args=[str(self.id)])
    
class WiFiQRCode(QRCodeBase):
    ENCRYPTION_CHOICES = [
        ('none', 'None'),
        ('wpa', 'WPA/WPA2'),
        ('wep', 'WEP'),
    ]
    ssid = models.CharField(max_length=50, verbose_name='Network Name')
    hidden = models.BooleanField(default=False, verbose_name='Hidden Network')
    password = models.CharField(max_length=50, verbose_name='Password')
    encryption = models.CharField(
        max_length=4,
        choices=ENCRYPTION_CHOICES,
        default='none',
        verbose_name='Encryption',
    )
    
    def get_qr_code_content(self):
        ssid = self.ssid
        hidden = "H:true;" if self.hidden else "H:false;"
        encryption = "T:WPA;" if self.encryption == 'wpa' else "T:WEP;" if self.encryption == 'wep' else "T:NONE;"
        password = f"P:{self.password};"
        wifi_uri = f'WIFI:S:{ssid};{hidden}{encryption}{password};;'
        return wifi_uri
    
    class Meta:
        verbose_name = 'WiFi QR Code'
        verbose_name_plural = 'WiFi'


    def save(self, *args, **kwargs):
        self.get_qr_code_content()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'WiFi QR Code: {self.ssid}'

    def get_absolute_url(self):
        return reverse('wifi_qr_code_detail', args=[str(self.id)])


class SocialMediaQRCode(QRCodeBase):
    SOCIAL_MEDIA_CHOICES = [
        ('Twitter', 'Twitter'),
        ('Facebook', 'Facebook'),
    ]

    TYPE_CHOICES = [
        ('Profile', 'Profile'),
        ('Post', 'Post'),
        ('Username', 'Username'),
    ]
    
    social_media = models.CharField(max_length=10, choices=SOCIAL_MEDIA_CHOICES, verbose_name='Social Media Platform')
    type = models.CharField(max_length=8, choices=TYPE_CHOICES, default='Profile')
    profile = models.CharField(max_length=255, blank=True, null=True, verbose_name='Profile')
    post = models.CharField(max_length=280, blank=True, null=True, verbose_name='Post Content')
    username = models.CharField(max_length=15, blank=True, null=True, verbose_name='Username')
    class Meta:
        verbose_name = 'Social Media QR Code'
        verbose_name_plural = 'Social Media'

    def get_qr_code_content(self):
        if self.social_media == 'Twitter':
            if self.type == 'Profile':
                content = f'https://twitter.com/{self.profile}'
            elif self.type == 'Post':
                content = f'https://twitter.com/intent/tweet?text={self.post}'
            elif self.type == 'Username':
                content = self.username
        elif self.social_media == 'Facebook':
            if self.type == 'Profile':
                content = self.profile
            elif self.type == 'Post':
                content = f'https://www.facebook.com/sharer/sharer.php?u={self.profile}&quote={self.post}'
            elif self.type == 'Username':
                content = self.username
        return content
    def __str__(self):
        return f'{self.social_media} QR Code: {self.get_qr_code_content()}'



class PdfQRCode(QRCodeBase):
    pdf_file = models.FileField(upload_to='files/pdf/', verbose_name='PDF File')

    class Meta:
        verbose_name = 'PDF QR Code'
        verbose_name_plural = 'PDF'

    def __str__(self):
        return f'PDF QR Code: {self.pdf_file.name}'

    def get_qr_code_content(self):
        return self.pdf_file.url


class MP3QRCode(QRCodeBase):
    title = models.CharField(max_length=255, verbose_name='Title')
    artist = models.CharField(max_length=255, verbose_name='Artist')
    audio_file = models.FileField(upload_to='files/audio/', verbose_name='Audio File')
    
    class Meta:
        verbose_name = 'MP3 QR Code'
        verbose_name_plural = 'MP3'


    def __str__(self):
        return self.title

    def get_qr_code_content(self):
        return self.audio_file.url

    def get_absolute_url(self):
        return reverse('mp3_qr_code_detail', args=[str(self.id)])
    
class AppStoreQRCode(QRCodeBase):
    app_name = models.CharField(max_length=255, verbose_name='App Name')
    platform = models.CharField(max_length=50, verbose_name='Platform')
    app_url = models.URLField(verbose_name='App URL')
    
    class Meta:
        verbose_name = 'App Store QR Code'
        verbose_name_plural = 'App Store'


    def __str__(self):
        return self.app_name

    def get_qr_code_content(self):
        return self.app_url

    def get_absolute_url(self):
        return reverse('app_store_qr_code_detail', args=[str(self.id)])

