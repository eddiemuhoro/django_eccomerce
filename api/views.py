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
    
class MpesaCallbackView(APIView):
    def post(self, request):
        serializer = MpesaPaymentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        
        # Process the callback data here
        callback = serializer.validated_data['Body']['stkCallback']
        result_code = callback['ResultCode']

        if result_code == 0:
            metadata = callback['CallbackMetadata']['Item']
            amount = metadata[0]['Value']
            phone_number = metadata[1]['Value']
            transaction_id = metadata[3]['Value']
           

            return Response({"message": "Callback processed successfully"}, status=200)
        
        return Response({"error": "Callback processing failed"}, status=400)
