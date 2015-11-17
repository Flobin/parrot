from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.models import ContentType

from posts.models import Link, Comment

class LinkModelTest(TestCase):

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

    def test_link_score_is_upvotes_minus_downvotes(self):
        link = Link.objects.create(title='poop',url='http://poop.bike',upvotes=5,downvotes=3)
        self.assertEqual(link.score(),2)

class CommentModelTest(TestCase):
    def test_comment_belongs_to_link(self):
        link = Link.objects.create(title='poop',url='http://google.com')
        comment = Comment(text='butt',content_object=link)
        comment.link = link
        comment.save()
        self.assertIn(comment, Comment.objects.filter(object_id = link.id, content_type=ContentType.objects.get_for_model(link)))

    def test_comment_score_is_upvotes_minus_downvotes(self):
        link = Link.objects.create(title='butt',url='http://poop.bike')
        comment = Comment(text='fart',content_object=link,upvotes=5,downvotes=3)
        comment.link = link
        self.assertEqual(comment.score(),2)

    def test_comment_can_belong_to_other_comment(self):
        link = Link.objects.create(title='poop',url='http://google.com')
        top_level_comment = Comment(text='butt',content_object=link)
        top_level_comment.link = link
        top_level_comment.save()
        second_level_comment = Comment(text='butt',content_object=top_level_comment)
        second_level_comment.top_level_comment = top_level_comment
        second_level_comment.save()
        self.assertIn(
            top_level_comment,
            Comment.objects.filter(
                object_id = link.id,
                content_type=ContentType.objects.get_for_model(link)
            )
        )
        self.assertIn(
            second_level_comment,
            Comment.objects.filter(
                object_id = top_level_comment.id,
                content_type=ContentType.objects.get_for_model(top_level_comment)
            )
        )
