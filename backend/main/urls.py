from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView
from rest_framework.routers import DefaultRouter

from library.views import AuthorViewSet, BookViewSet, GenreViewSet
from user.views import UserViewSet, CommentViewSet, ReadingViewSet

router = DefaultRouter()

router.register(r'authors', AuthorViewSet, 'authors')
router.register(r'books', BookViewSet, 'books')
router.register(r'genres', GenreViewSet, 'genres')
router.register(r'users', UserViewSet, 'users')
router.register(r'comments', CommentViewSet, 'comments')
router.register(r'readings', ReadingViewSet, 'readings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls.authtoken')),
]

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
