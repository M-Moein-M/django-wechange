from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import Profile


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        read_only_fields = ['id']


class ProfileSerializer(serializers.ModelSerializer):
    """Serializer for Profile model"""
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['id', 'picture']

    def update(self, instance, validated_data):
        user_data = validated_data.get('user')
        if user_data:
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.save()

        instance.about = validated_data.get('about', instance.about)
        instance.save()
        return instance
