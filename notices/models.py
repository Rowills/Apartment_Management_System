from django.conf import settings
from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    published_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='published_notices')
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
