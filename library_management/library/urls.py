# library/urls.py
from django.urls import path
from .views import admin_signup, admin_login, book_list_create, book_detail, student_books, home

urlpatterns = [
    path('', home, name='home'),  # Home route
    path('admin/signup/', admin_signup, name='admin-signup'),
    path('admin/login/', admin_login, name='admin-login'),
    path('api/books/', book_list_create, name='book-list'),
    path('api/books/<int:pk>/', book_detail, name='book-detail'),
    path('student/books/', student_books, name='student-books'),
]
