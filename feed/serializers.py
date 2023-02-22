from rest_framework import serializers
from useraccount.models import User


from .models import Post, Comment, PostLike

class AuthorSerializer(serializers.ModelSerializer):
    """ This serializers is just for adding it to the Post and Comment Serailizers. """
    class Meta:
        model = User
        exclude = ['password']

class PostForCommentSerializer(serializers.ModelSerializer):
    """ This serializers is just for adding it to the Comment Serailizers. """
    class Meta:
        model = Post
        fields = "__all__"

class PostLikeSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PostLike
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    active = serializers.BooleanField(read_only=True)
    post_of_comment = PostForCommentSerializer(source="post" ,read_only=True)
    author_of_comment = AuthorSerializer(source="author", read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comment_on_post = CommentSerializer(many=True, read_only=True)
    liked_post = PostLikeSerializer(many=True, read_only=True)
    author_of_post = AuthorSerializer(source='author', read_only=True)

    author = serializers.StringRelatedField(read_only=True)
    active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'