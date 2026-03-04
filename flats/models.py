from django.conf import settings
from django.db import models


class Flat(models.Model):
    number = models.CharField(max_length=20, unique=True)
    block = models.CharField(max_length=20)
    floor = models.PositiveIntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_flats', on_delete=models.PROTECT)
    resident = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='occupied_flats', on_delete=models.PROTECT)
    ownership_document = models.FileField(upload_to='documents/flats/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['block', 'number']

    def __str__(self):
        return f'{self.block}-{self.number}'
