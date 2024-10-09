from rest_framework import serializers
from .models import Item
from django.contrib.auth.models import User

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']  # Add any other fields you need, like email

    # Custom create method to handle password hashing
    def create(self, validated_data):
        # The create_user method ensures the password is hashed
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user