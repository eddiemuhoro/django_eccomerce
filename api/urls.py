from .views import MpesaTokenView, MpesaPaymentView, MpesaCallbackView
from django.urls import path

urlpatterns = [
    path('token/', MpesaTokenView.as_view(), name='mpesa_token'),
    path('pay/', MpesaPaymentView.as_view(), name='mpesa_payment'),
    path('callback/', MpesaCallbackView.as_view(), name='mpesa_callback')
    ]