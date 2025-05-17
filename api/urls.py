from .views import MpesaTokenView, MpesaPaymentView
from django.urls import path

urlpatterns = [
    path('token/', MpesaTokenView.as_view(), name='mpesa_token'),
    path('pay/', MpesaPaymentView.as_view(), name='mpesa_payment'),
]