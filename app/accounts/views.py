from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts import serializers
from django.contrib.auth import authenticate, login


class CreateUserView(generics.CreateAPIView):
    """Handle user objects"""
    serializer_class = serializers.UserSerializer


class LoginUserView(APIView):
    """Handle user login"""

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
