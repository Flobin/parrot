from django.db import models
from django.utils import timezone

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=140)
    url = models.URLField(unique=True)
    posted = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def score(self):
        return self.upvotes - self.downvotes

    def __str__(self):
        return self.title
