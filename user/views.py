from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from djoser.views import UserViewSet as DjoserUserViewSet

from main.permissions import IsStaffOrReadOnly, IsAuthor
from user.models import Comment

from user.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsStaffOrReadOnly, IsAuthor)


class UserViewSet(DjoserUserViewSet):
    lookup_field = 'username'

    @action(methods=['GET'], detail=True)
    def comments(self, request, username):
        serialized = CommentSerializer(Comment.objects.filter(user__username=username), many=True)
        return Response(serialized.data)
