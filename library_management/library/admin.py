# library/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Admin, Book

class AdminUserAdmin(UserAdmin):
    model = Admin
    list_display = ('email', 'username', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')

admin.site.register(Admin, AdminUserAdmin)
admin.site.register(Book)
