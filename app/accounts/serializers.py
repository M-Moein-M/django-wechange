from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        read_only_fields = ['id', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model"""
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),
                                              required=False)

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id', 'picture']
