from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

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

class Comment(models.Model):
    text = models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def score(self):
        return self.upvotes - self.downvotes
