from django.test import TestCase
from django.core.exceptions import ValidationError

from posts.models import Link, Comment

class LinksAndCommentsModelsTest(TestCase):

    def test_can_create_links(self):
        link = Link.objects.create(title='poop',url='http://google.com')
        self.assertEqual(Link.objects.count(), 1)

    def test_default_text(self):
        link = Link()
        self.assertEqual(link.title, '')

    def test_empty_links_not_allowed(self):
        link = Link.objects.create(title='',url='')
        with self.assertRaises(ValidationError):
            link.save()
            link.full_clean()

    def test_score_is_upvotes_minus_downvotes(self):
        link = Link.objects.create(title='poop',url='http://poop.bike',upvotes=5,downvotes=3)
        self.assertEqual(link.score(),2)

    def test_comment_belongs_to_link(self):
        link = Link.objects.create(title='poop',url='http://google.com')
        comment = Comment(text='butt',content_object=Link)
        comment.link = link
        comment.save()
        self.assertIn(comment, link.comment_set.all())
