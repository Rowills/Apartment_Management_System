from django.db import models

from flats.models import Flat


class VisitorLog(models.Model):
    visitor_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=20)
    purpose = models.CharField(max_length=255)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='visitor_logs')
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-entry_time']

    def __str__(self):
        return f'{self.visitor_name} - {self.flat}'
