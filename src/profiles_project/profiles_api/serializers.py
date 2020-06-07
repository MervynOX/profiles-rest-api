from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=50) #logic will be automatically provided, therefore error handling not needed


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile # tell django what model we are using
        fields = ('id','email', 'name', 'password') # what field in the model that we want to use in the serializer
        extra_kwargs = {'password': {'write_only': True}} # special attri that we want to apply.... e.g. pw is WRITE only for security

    # assign pw properly to the user
    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed item."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}} # create profile feed item for the currently logged in user