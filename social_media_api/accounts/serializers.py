from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure CharField is explicitly used

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """Create a user using create_user to hash the password properly."""
        user = get_user_model().objects.create_user(  # Ensure create_user is explicitly used
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Generate auth token for the user
        return user
