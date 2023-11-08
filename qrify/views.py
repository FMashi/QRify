from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import UrlQrCode, TextQrCode
from .forms import UrlQrCodeForm, TextQrCodeForm  
from django.utils.encoding import uri_to_iri 
from .serializers import UrlQrCodeSerializer, TextQrCodeSerializer
from rest_framework import generics

class UrlQrCodeCreateView(generics.CreateAPIView):
    queryset = UrlQrCode.objects.all()
    serializer_class = UrlQrCodeSerializer
    
class TextQrCodeCreateView(generics.CreateAPIView):
    queryset = TextQrCode.objects.all()
    serializer_class = TextQrCodeSerializer
 
# class UrlQrCodeListCreateView(generics.ListCreateAPIView):
#     queryset = UrlQrCode.objects.all()
#     serializer_class = UrlQrCodeSerializer

# class TextQrCodeListCreateView(generics.ListCreateAPIView):
#     queryset = TextQrCode.objects.all()
#     serializer_class = TextQrCodeSerializer
# class UrlQrCodeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UrlQrCode.objects.all()
#     serializer_class = UrlQrCodeSerializer
# class TextQrCodeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = TextQrCode.objects.all()
#     serializer_class = TextQrCodeSerializer

    
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
