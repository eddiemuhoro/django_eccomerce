from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django_daraja.mpesa.core import MpesaClient
from .utils import get_access_token, lipa_na_mpesa_online
from .serializers import MpesaPaymentSerializer

# Create your views here.
class MpesaTokenView(APIView):
    def get(self, request):
        try:
            token = get_access_token()
            return Response({"access_token": token}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class MpesaPaymentView(APIView):
    def post(self, request):
        serializer = MpesaPaymentSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            amount = serializer.validated_data['amount']
            response = lipa_na_mpesa_online(phone_number, amount)
            return Response(response, status=200)
        return Response(serializer.errors, status=400)