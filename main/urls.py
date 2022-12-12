from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.shortcuts import redirect
from django.urls import path, include
from django.views.decorators.cache import never_cache

from rest_framework.routers import DefaultRouter

from library.views import AuthorViewSet, BookViewSet, GenreViewSet
from user.views import UserViewSet, CommentViewSet, ReadingViewSet
from .yasg import urlpatterns as docs_urls

router = DefaultRouter()

router.register(r'authors', AuthorViewSet, 'authors')
router.register(r'books', BookViewSet, 'books')
router.register(r'genres', GenreViewSet, 'genres')
router.register(r'users', UserViewSet, 'users')
router.register(r'comments', CommentViewSet, 'comments')
router.register(r'readings', ReadingViewSet, 'readings')


def index(request):
    return redirect('api/')


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),
]

urlpatterns += docs_urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
