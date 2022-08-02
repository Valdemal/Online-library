from django.urls import path
from .views import BookListAPIView, AuthorAPIView, AuthorListAPIView

app_name = 'api'

urlpatterns = [
    path('book/', BookListAPIView.as_view()),
    path('author/', AuthorListAPIView.as_view()),
    path('author/<int:pk>/', AuthorAPIView.as_view()),
]
