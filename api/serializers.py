from rest_framework import serializers

from page.models import Post, MyUser


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
