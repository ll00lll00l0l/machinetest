from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Driver,Ride

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
class RiderSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

    def to_representation(self, instance):
        return instance.username
        
class RideSerializer(serializers.ModelSerializer):
    rider = RiderSerial()
    class Meta:
        model = Ride
        fields = '__all__'
