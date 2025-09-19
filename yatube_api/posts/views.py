from rest_framework import permissions, serializers, viewsets
from django.shortcuts import get_object_or_404
from posts.models import Follow
from .serializers import FollowSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        following_id = self.request.data.get('following')
        following = get_object_or_404(User, id=following_id)

        if following == self.request.user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя'
            )

        serializer.save(user=self.request.user, following=following)
