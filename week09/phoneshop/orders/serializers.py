from rest_framework import serializers
from .models import Orders
from django.contrib.auth.models import User

class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = ['id', 'order_name', 'order_number', 'order_status', 'created_time', 'owner']

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Orders.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']