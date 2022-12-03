from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import mixins
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from main.permissions import IsStaffOrReadOnly, IsAuthor, CanCreateIfAuthenticated, IsStaff
from user.models import Comment, Reading
from user.serializers import CommentGetSerializer, CommentSetSerializer, ReadingGetSerializer, ReadingSetSerializer


class UserViewSet(DjoserUserViewSet):
    lookup_field = 'username'

    # IsStaff
    @permission_classes([IsStaff])
    @action(methods=['GET'], detail=True)
    def comments(self, request, username):
        serialized = CommentGetSerializer(Comment.objects.filter(user__username=username), many=True)
        return Response(serialized.data)

    # IsStaff
    @action(methods=['GET'], detail=True)
    def readings(self, request, username):
        serialized = ReadingGetSerializer(Reading.objects.filter(user__username=username), many=True)
        return Response(serialized.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    # Заебало
    permission_classes = [((IsStaffOrReadOnly | CanCreateIfAuthenticated) | IsAuthor), ]

    def get_serializer_class(self):
        return CommentGetSerializer if self.request.method in SAFE_METHODS else CommentSetSerializer


class ReadingViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Reading.objects.all()

    def get_serializer_class(self):
        return ReadingGetSerializer if self.request.method in SAFE_METHODS else ReadingSetSerializer

