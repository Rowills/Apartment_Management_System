from django.contrib import admin

from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'flat', 'category', 'status', 'raised_by', 'assigned_to')
    list_filter = ('status', 'category')
