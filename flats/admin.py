from django.contrib import admin

from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    list_display = ('number', 'block', 'floor', 'owner', 'resident')
    search_fields = ('number', 'block')
