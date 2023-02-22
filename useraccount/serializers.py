from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers

from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer

from .models import User
from feed.serializers import PostSerializer, CommentSerializer

User = get_user_model()

class CustomTokenCreateSerializer(TokenCreateSerializer):

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
        # We changed only below line
        if self.user: # and self.user.is_active: 
            return attrs
        self.fail("invalid_credentials")

class UpdateProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['imagefield']


class BasicInfoSerializer(serializers.ModelSerializer):
    postlist_author = PostSerializer(many=True, read_only=True)
    commentlist_author = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ['password']

class AdminInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'username', 'email']

