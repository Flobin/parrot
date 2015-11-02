from django.db import models

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=140)
    url = models.URLField()

    def __str__(self):
        return self.title