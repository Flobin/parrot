from django.db import models
from django.utils import timezone

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=140)
    url = models.URLField()
    posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
