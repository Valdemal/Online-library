from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from djoser.views import UserViewSet as DjoserUserViewSet

from main.permissions import IsStaffOrReadOnly, IsAuthor
from user.models import Comment, Reading

from user.serializers import CommentSerializer, ReadingSerializer


class UserViewSet(DjoserUserViewSet):
    lookup_field = 'username'

    @action(methods=['GET'], detail=True)
    def comments(self, request, username):
        serialized = CommentSerializer(Comment.objects.filter(user__username=username), many=True)
        return Response(serialized.data)

    @action(methods=['GET'], detail=True)
    def readings(self, request, username):
        serialized = ReadingSerializer(Reading.objects.filter(user__username=username), many=True)
        return Response(serialized.data)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsStaffOrReadOnly, IsAuthor)


class ReadingViewSet(ModelViewSet):
    serializer_class = ReadingSerializer
    queryset = Reading.objects.all()
    permission_classes = (IsStaffOrReadOnly, IsAuthor)
