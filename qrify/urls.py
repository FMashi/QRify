from django.urls import path
from .import views

app_name = 'qrify'

urlpatterns = [
    path('qrify/', views.qr_code_list, name='qr_code_list'),
    path('qrify/create/url/', views.create_url_qr_code, name='create_url_qr_code'),
    path('qrify/create/text/', views.create_text_qr_code, name='create_text_qr_code'),
    path('qrify/<int:qr_code_id>/', views.qr_code_detail, name='qr_code_detail'),
    
    # api
    #Create 
    path('api/url/create/', views.UrlQrCodeCreateView.as_view(), name='url'),
    path('api/text/create/', views.TextQrCodeCreateView.as_view(), name='text'),
    path('api/phone/create/', views.PhoneQrCodeCreateView.as_view(), name='phone'),
    path('api/vcard/create/', views.VCardQRCodeCreateView.as_view(), name='vcard'),
    path('api/email/create/', views.EmailQRCodeCreateView.as_view(), name='email'),
    path('api/sms/create/', views.SMSQRCodeCreateView.as_view(), name='sms'),
    path('api/wifi/create/', views.WiFiQRCodeCreateView.as_view(), name='wifi'),
    path('api/socialmedia/create/', views.SocialMediaQRCodeCreateView.as_view(), name='socialmedia'),
    path('api/pdf/create/', views.PdfQRCodeCreateView.as_view(), name='pdf'),
    path('api/mp3/create/', views.MP3QRCodeCreateView.as_view(), name='mp3'),
    path('api/appstore/create/', views.AppStoreQRCodeCreateView.as_view(), name='appstore'),


    #Detail
    # path('api/url-qr-codes/<int:pk>/', views.UrlQrCodeRetrieveUpdateDestroyView.as_view(), name='url_qr_code_detail'),
    # path('api/text-qr-codes/<int:pk>/', views.TextQrCodeRetrieveUpdateDestroyView.as_view(), name='text_qr_code_detail'),
    #List
    # path('api/url-qr-codes/', views.UrlQrCodeListCreateView.as_view(), name='url_qr_code_list_create'),
    # path('api/text-qr-codes/', views.TextQrCodeListCreateView.as_view(), name='text_qr_code_list_create'),
]
