from rest_framework import serializers
from .models import User, Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'user','content', 'image', 'created_at', 'likes_count'] 
        read_only_fields = ['id', 'user','created_at', 'likes_count']

    def validate(self, attrs):
        if not attrs.get('content') and not attrs.get('image'):
            raise serializers.ValidationError("At least one of 'content' or 'image' must be provided.")
        return attrs


class FollowingUserSerializar(serializers.ModelSerializer):

    tweets = TweetSerializer(many=True, read_only=True)

    class Meta:
        model= User
        fields = ['id', 'username', 'tweets']
        read_only_fields = ['id', 'tweets']

class FollowerUserSerializar(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_confirm')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        # Verifica se a senha e a confirmação da senha são iguais
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDetailSerializer(serializers.ModelSerializer):
    tweets = TweetSerializer(many=True, read_only=True)
    followers = FollowerUserSerializar(many=True, read_only=True)
    following = FollowingUserSerializar(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'followers', 'following', 'tweets' ) 
