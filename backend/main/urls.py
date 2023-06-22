from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions
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

schema_view = get_schema_view(
    openapi.Info(
        title="Online-library",
        default_version="v1",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ]
)

urlpatterns += [
    path('openapi', schema_view.as_view(), name='openapi-schema'),
    path('api/swagger/', TemplateView.as_view(
        template_name='../templates/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
