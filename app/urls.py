from django.urls import path
from .views import BookList, CreateBook

urlpatterns = [
    path('', BookList.as_view(), name='books'),
    path('add-book/', CreateBook.as_view(), name='add-book')
]
