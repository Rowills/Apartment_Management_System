from django.contrib import admin

from .models import VisitorLog


@admin.register(VisitorLog)
class VisitorLogAdmin(admin.ModelAdmin):
    list_display = ('visitor_name', 'phone_number', 'flat', 'entry_time', 'exit_time')
    search_fields = ('visitor_name', 'phone_number')
