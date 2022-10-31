from rest_framework import serializers
from django.contrib.auth.models import User

from accounts.models import Score

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class ScoreSerializer(serializers.ModelSerializer):
	player = serializers.SlugRelatedField(queryset = User.objects.all(),slug_field = 'id')
	class Meta:
		model = Score
		fields = ['id','highest_score','total_questions','current_score','right_attempt','wrong_attempt','player']
		depth = 1