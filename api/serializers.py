from rest_framework import serializers
from orders.models import Order

class MpesaPaymentSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    amount = serializers.IntegerField()

class MpesaCallbackSerializer(serializers.Serializer):
    Body = serializers.DictField()
    
class CreateCheckoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'cart', 'total_price', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        checkout = Order.objects.create(**validated_data)
        return checkout