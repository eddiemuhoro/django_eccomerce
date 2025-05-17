from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django_daraja.mpesa.core import MpesaClient
from .utils import get_access_token

# Create your views here.
class MpesaTokenView(APIView):
    def get(self, request):
        try:
            token = get_access_token()
            return Response({"access_token": token}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)