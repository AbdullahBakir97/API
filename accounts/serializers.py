from rest_framework import serializers
from .models import Team, Player, Match, FantasyTeam, Contest, ContestEntry
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()

class SignupSerializer(serializers.Serializer):
    """Serializer for user signup."""
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        """Check if email already exists."""
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email address already exists")
        return value

    def create(self, validated_data):
        """Create new user."""
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""
    username = serializers.CharField()
    password = serializers.CharField()

class ChangePasswordSerializer(serializers.Serializer):
    """Serializer for changing password."""
    old_password = serializers.CharField()
    new_password = serializers.CharField()

class PasswordResetSerializer(serializers.Serializer):
    """Serializer for password reset."""
    email = serializers.EmailField()

class PasswordResetConfirmSerializer(serializers.Serializer):
    """Serializer for confirming password reset."""
    token = serializers.CharField()
    new_password = serializers.CharField()


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class FantasyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam
        fields = '__all__'

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contest
        fields = '__all__'

class ContestEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestEntry
        fields = '__all__'
