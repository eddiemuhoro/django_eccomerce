from rest_framework import serializers

class MpesaPaymentSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)

class MpesaCallbackSerializer(serializers.Serializer):
    Body = serializers.DictField()