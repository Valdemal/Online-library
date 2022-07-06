from django.urls import path
from .views import BookListAPIView, AuthorAPIView

app_name = 'library'

urlpatterns = [
    path('api/booklist/', BookListAPIView.as_view()),
    path('api/author/<int:pk>/', AuthorAPIView.as_view()),
]
