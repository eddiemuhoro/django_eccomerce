from .views import MpesaTokenView
from django.urls import path

urlpatterns = [
    path('token/', MpesaTokenView.as_view(), name='mpesa_token'),
]