from djoser.views import UserViewSet as DjoserUserViewSet
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from main.permissions import IsAuthorOrStaff
from user.filters import ReadingFilter, CommentFilter
from user.models import Comment, Reading
from user.serializers import CommentGetSerializer, CommentSetSerializer, ReadingGetSerializer, ReadingSetSerializer


class UserViewSet(DjoserUserViewSet):
    lookup_field = 'username'

    @action(methods=['GET'], url_path='me/comments', detail=False)
    def my_comments(self, request):
        serialized = CommentGetSerializer(Comment.objects.filter(user=request.user), many=True)
        return Response(serialized.data)

    @action(methods=['GET'], url_path='me/readings', detail=False)
    def my_readings(self, request):
        serialized = ReadingGetSerializer(Reading.objects.filter(user=request.user), many=True)
        return Response(serialized.data)

    def get_permissions(self):
        if self.action in ('my_comments', 'my_readings'):
            return IsAuthenticated(),

        return super().get_permissions()


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    filterset_class = CommentFilter

    def get_serializer_class(self):
        return CommentGetSerializer if self.request.method in SAFE_METHODS else CommentSetSerializer

    def get_permissions(self):
        if self.action == 'list':
            return AllowAny(),
        elif self.action == 'create':
            return IsAuthenticated(),
        else:
            return IsAuthorOrStaff(),


class ReadingViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = Reading.objects.all()
    filterset_class = ReadingFilter

    def get_serializer_class(self):
        return ReadingGetSerializer if self.request.method in SAFE_METHODS else ReadingSetSerializer

    def get_permissions(self):
        if self.action == 'create':
            return IsAuthenticated(),
        elif self.action == 'destroy':
            return IsAuthorOrStaff(),
        else:
            return IsAdminUser(),
