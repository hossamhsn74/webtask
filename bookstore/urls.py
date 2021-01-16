from django.urls import path
from .api import views

# /books >> get, post
# /books/id >>get,put,delete,patch

urlpatterns = [
    path('', views.BookListView.as_view(), name='booklist'),
    path('create/', views.BookCreateView.as_view(), name='createbook'),
    path('<str:title>/', views.BookDetailView.as_view(), name='updatebook'),
    path('hello/', views.HelloView.as_view(), name='hello'),

]