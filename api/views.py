from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers import PostSerializer, VoteSerializer
from page.models import Post, Vote


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        post = Post.objects.filter(id=serializer.validated_data.get("post_id"))

        if post.exists():
            if post.first().vote.filter(user=self.request.user).exists() is False:
                serializer.save(user=self.request.user,
                                post=post.first(),
                                vote=True)
            else:
                post.first().vote.get(user=self.request.user).delete()
