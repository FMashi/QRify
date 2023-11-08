import os
from django.utils import timezone
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image
from ckeditor.fields import RichTextField
import uuid 
from django.utils.html import strip_tags,escape
from html2text import html2text

def qr_code_upload_path(instance, filename):
    folder_name = timezone.now().strftime('%Y/%m/%d')
    if isinstance(instance, UrlQrCode):
        subfolder_name = 'url'
    elif isinstance(instance, TextQrCode):
        subfolder_name = 'text'
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

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.get_qr_code_content())
        canvas = Image.new("RGB", (410, 410), "white")
        canvas.paste(qrcode_img)
        fname = self.generate_unique_filename()
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.image.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class UrlQrCode(QRCodeBase):
    url = models.URLField(blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.url

    def get_qr_code_content(self):
        return self.url

class TextQrCode(QRCodeBase):
    text = RichTextField(blank=True, null=True, verbose_name='Text Content')

    def __str__(self):
        return strip_tags(self.text)

    def get_qr_code_content(self):
        plain_text = strip_tags(self.text)
        return escape(plain_text)
