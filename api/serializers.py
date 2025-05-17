from rest_framework import serializers

class MpesaPaymentSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    amount = serializers.IntegerField()

class MpesaCallbackSerializer(serializers.Serializer):
    Body = serializers.DictField()