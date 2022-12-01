from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from library.views import AuthorViewSet, BookViewSet, GenreViewSet

from user.views import UserViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, 'authors')
router.register(r'books', BookViewSet, 'books')
router.register(r'genres', GenreViewSet, 'genres')
router.register(r'users', UserViewSet, 'users')
router.register(r'comments', CommentViewSet, 'comments')

def index(request):
    return redirect('api/')


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
