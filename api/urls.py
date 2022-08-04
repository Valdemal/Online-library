from django.urls import path

from .views import BookListAPIView, AuthorAPIView, AuthorListAPIView, BookAPIView, AuthorBooksAPIView

app_name = 'api'

urlpatterns = [
    path('books/', BookListAPIView.as_view()),
    path('books/<int:pk>/', BookAPIView.as_view()),
    path('authors/', AuthorListAPIView.as_view()),
    path('authors/<int:pk>/', AuthorAPIView.as_view()),
    path('authors/<int:pk>/books/', AuthorBooksAPIView.as_view())
]
