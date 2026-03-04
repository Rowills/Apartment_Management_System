from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Community Info', {'fields': ('role', 'phone_number', 'is_approved')}),
    )
    list_display = ('username', 'email', 'role', 'is_approved', 'is_staff')
