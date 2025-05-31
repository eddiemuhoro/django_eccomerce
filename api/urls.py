from .views import MpesaTokenView, MpesaPaymentView, MpesaCallbackView, CreateCheckoutSessionView, GetStripePublishableKeyView
from django.urls import path

urlpatterns = [
    path('token/', MpesaTokenView.as_view(), name='mpesa_token'),
    path('pay/mpesa/', MpesaPaymentView.as_view(), name='mpesa_payment'),
    path('pay/stripe/', CreateCheckoutSessionView.as_view(), name='mpesa_payment'),
    path('pay/create-checkout-session/', GetStripePublishableKeyView.as_view(), name='create-checkout-session'),

    path('callback/', MpesaCallbackView.as_view(), name='mpesa_callback')
    ]