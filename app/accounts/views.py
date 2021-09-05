from rest_framework import generics
from accounts import serializers


class CreateUserView(generics.CreateAPIView):
    """Handle user objects"""
    serializer_class = serializers.UserSerializer
