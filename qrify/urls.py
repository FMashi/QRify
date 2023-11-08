from django.urls import path
from . import views

app_name = 'qrify'

urlpatterns = [
    path('qrify/', views.qr_code_list, name='qr_code_list'),
    path('qrify/create/url/', views.create_url_qr_code, name='create_url_qr_code'),
    path('qrify/create/text/', views.create_text_qr_code, name='create_text_qr_code'),
    path('qrify/<int:qr_code_id>/', views.qr_code_detail, name='qr_code_detail'),
]
