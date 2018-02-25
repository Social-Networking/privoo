from rest_framework import serializers

from page.models import Post, MyUser, Vote


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('id', 'name', 'avatar')

    def get_name(self, obj):
        return obj.get_name()


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, read_only=True)
    created = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = ('description', 'owner', 'created')


class VoteSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    vote = serializers.BooleanField(read_only=True)
    post_id = serializers.IntegerField()

    class Meta:
        model = Vote
        fields = ('user', 'date', 'vote', 'post_id')
