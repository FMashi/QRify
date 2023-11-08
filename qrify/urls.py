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
    path('api/url-qr-codes/create/', views.UrlQrCodeCreateView.as_view(), name='url_qr_code_create'),
    path('api/text-qr-codes/create/', views.TextQrCodeCreateView.as_view(), name='text_qr_code_create'),


    #Detail
    # path('api/url-qr-codes/<int:pk>/', views.UrlQrCodeRetrieveUpdateDestroyView.as_view(), name='url_qr_code_detail'),
    # path('api/text-qr-codes/<int:pk>/', views.TextQrCodeRetrieveUpdateDestroyView.as_view(), name='text_qr_code_detail'),
    #List
    # path('api/url-qr-codes/', views.UrlQrCodeListCreateView.as_view(), name='url_qr_code_list_create'),
    # path('api/text-qr-codes/', views.TextQrCodeListCreateView.as_view(), name='text_qr_code_list_create'),
]
