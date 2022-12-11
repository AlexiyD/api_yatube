from posts.models import Comment, Group, Post
from rest_framework.serializers import ModelSerializer, SlugRelatedField


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post',)


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(
        read_only=True, slug_field='username'
    )
    group = SlugRelatedField(
        read_only=True, slug_field='title'
    )

    class Meta:
        model = Post
        fields = '__all__'
