from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from mptt.models import MPTTModel, TreeForeignKey

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

class Comment(MPTTModel):
    text = models.TextField()
    posted = models.DateTimeField(default=timezone.now)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    link = models.ForeignKey('Link', related_name='comments')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)

    def score(self):
        return self.upvotes - self.downvotes

    def __str__(self):
        return "Comment {0}, refers to {1}, parent is {2}".format(self.id,self.link,self.parent)
