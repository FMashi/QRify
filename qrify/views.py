from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UrlQrCodeForm, TextQrCodeForm  
from django.utils.encoding import uri_to_iri 
from .serializers import UrlQrCodeSerializer, TextQrCodeSerializer
from rest_framework import generics,viewsets
from .models import (
    UrlQrCode,
    TextQrCode,
    PhoneQrCode,
    VCardQRCode,
    EmailQRCode,
    SMSQRCode,
    WiFiQRCode,
    SocialMediaQRCode,
    PdfQRCode,
    MP3QRCode,
    AppStoreQRCode,
)
from .serializers import (
    UrlQrCodeSerializer,
    TextQrCodeSerializer,
    PhoneQrCodeSerializer,
    VCardQRCodeSerializer,
    EmailQRCodeSerializer,
    SMSQRCodeSerializer,
    WiFiQRCodeSerializer,
    SocialMediaQRCodeSerializer,
    PdfQRCodeSerializer,
    MP3QRCodeSerializer,
    AppStoreQRCodeSerializer,
)

class UrlQrCodeCreateView(generics.CreateAPIView):
    queryset = UrlQrCode.objects.all()
    serializer_class = UrlQrCodeSerializer
    
class TextQrCodeCreateView(generics.CreateAPIView):
    queryset = TextQrCode.objects.all()
    serializer_class = TextQrCodeSerializer

class PhoneQrCodeCreateView(generics.CreateAPIView):
    queryset = PhoneQrCode.objects.all()
    serializer_class = PhoneQrCodeSerializer

class VCardQRCodeCreateView(generics.CreateAPIView):
    queryset = VCardQRCode.objects.all()
    serializer_class = VCardQRCodeSerializer

# Create viewsets for other models using the same pattern

class EmailQRCodeCreateView(generics.CreateAPIView):
    queryset = EmailQRCode.objects.all()
    serializer_class = EmailQRCodeSerializer

class SMSQRCodeCreateView(generics.CreateAPIView):
    queryset = SMSQRCode.objects.all()
    serializer_class = SMSQRCodeSerializer

class WiFiQRCodeCreateView(generics.CreateAPIView):
    queryset = WiFiQRCode.objects.all()
    serializer_class = WiFiQRCodeSerializer

class SocialMediaQRCodeCreateView(generics.CreateAPIView):
    queryset = SocialMediaQRCode.objects.all()
    serializer_class = SocialMediaQRCodeSerializer

class PdfQRCodeCreateView(generics.CreateAPIView):
    queryset = PdfQRCode.objects.all()
    serializer_class = PdfQRCodeSerializer

class MP3QRCodeCreateView(generics.CreateAPIView):
    queryset = MP3QRCode.objects.all()
    serializer_class = MP3QRCodeSerializer

class AppStoreQRCodeCreateView(generics.CreateAPIView):
    queryset = AppStoreQRCode.objects.all()
    serializer_class = AppStoreQRCodeSerializer
       
def qr_code_list(request):
    url_qr_codes = UrlQrCode.objects.all()
    text_qr_codes = TextQrCode.objects.all()
    context = {
        'title': 'qr code list',
        'url_qr_codes': url_qr_codes,
        'text_qr_codes': text_qr_codes,
    }
    template = 'qrify/qr_code_list.html'
    return render(request,template, context)

def create_url_qr_code(request):
    if request.method == 'POST':
        form = UrlQrCodeForm(request.POST)
        if form.is_valid():
            qr_code = form.save()
            return HttpResponseRedirect(qr_code.get_absolute_url()) 
    else:
        form = UrlQrCodeForm()
    context = {
        'title': 'create url qr code',
        'form': form
    }
    template = 'qrify/create_url_qr_code.html'
    return render(request, template,context)

def create_text_qr_code(request):
    if request.method == 'POST':
        form = TextQrCodeForm(request.POST)
        if form.is_valid():
            qr_code = form.save()
            return HttpResponseRedirect(qr_code.get_absolute_url()) 
    else:
        form = TextQrCodeForm()
    context = {
        'title': 'create text qr code',
        'form': form
    }
    template = 'qrify/create_text_qr_code.html'
    return render(request,template,context)

def qr_code_detail(request, qr_code_id):
    url_qr_code = get_object_or_404(UrlQrCode, pk=uri_to_iri(qr_code_id))
    text_qr_code = get_object_or_404(TextQrCode, pk=uri_to_iri(qr_code_id))
    context = {
        'title': 'create text qr code',
        'url_qr_code': url_qr_code,
        'text_qr_code': text_qr_code,
    }
    template = 'qrify/qr_code_detail.html'
    return render(request, template, context)
