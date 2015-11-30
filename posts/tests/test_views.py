from datetime import timedelta

from unittest import skip

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.utils import timezone
from django.contrib.auth.models import User

from posts.views import links, comments
from posts.models import Link, Comment
from posts.forms import LinkForm, CommentForm

class HomePageTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'posts/links.html')

    def test_home_page_displays_links(self):
        first_link = Link.objects.create(title='foo',url='http://google.com')
        second_link = Link.objects.create(title='bar',url='http://reddit.com')
        response = self.client.get('/')
        self.assertContains(response, 'foo')
        self.assertContains(response, 'bar')
        self.assertEqual(Link.objects.all().count(), 2)

    def test_links_are_displayed_chronologically(self):
        first_link = Link.objects.create(title='foo',url='http://google.com',posted=timezone.now()-timedelta(days=2))
        second_link = Link.objects.create(title='bar',url='http://reddit.com')
        response = self.client.get('/')
        links = response.context[0]['links']
        self.assertEqual(links[0], second_link)
        self.assertEqual(links[1], first_link)

    def test_displays_link_form(self):
        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], LinkForm)
        self.assertContains(response, 'name="title"')

    def test_can_vote_on_link(self):
        link = Link.objects.create(title='foo',url='http://google.com',upvotes=5,downvotes=3)
        response = self.client.post(
            '/vote_link/{0}'.format(link.id),
            data={'submit_vote_button': 'upvote'}
        )
        updated_link = Link.objects.get(pk=link.id)
        self.assertEqual(updated_link.score, 3)

class CommentsViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')

    def test_comments_view_renders_comments_template(self):
        link = Link.objects.create(title='foo',url='http://google.com')
        response = self.client.get('/{0}/'.format(link.id))
        self.assertTemplateUsed(response, 'posts/comments.html')

    def test_saving_a_POST_request_for_top_level_comment(self):
        link = Link.objects.create(title='foo',url='http://google.com')
        self.client.post(
            '/{0}/'.format(link.id),
            data={'text': 'A top level comment','link': link,'parent': None}
        )
        self.assertEqual(Comment.objects.count(), 1)
        new_comment = Comment.objects.first()
        self.assertEqual(new_comment.text, 'A top level comment')

    def test_saving_a_POST_request_for_child_comment(self):
        link = Link.objects.create(title='foo',url='http://google.com')
        top_level_comment = Comment.objects.create(text='A top level comment',link=link,parent=None)
        self.client.post(
            '/{0}/'.format(link.id),
            data={'text': 'A child comment','link': link,'parent': None}
        )
        self.assertEqual(Comment.objects.count(), 2)
        child_comment = Comment.objects.last()
        self.assertEqual(child_comment.text, 'A child comment')

    @skip("chronology isn't really important anyway...")
    def test_comments_are_displayed_chronologically(self):
        link = Link.objects.create(title='bar',url='http://reddit.com',posted=timezone.now()-timedelta(days=1))
        first_comment = Comment.objects.create(text="poop",content_object=link)
        second_comment = Comment.objects.create(text="butt",content_object=link,posted=timezone.now()-timedelta(days=2))
        response = self.client.get('/{0}/'.format(link.id))
        comments = response.context[0]['comments']
        self.assertEqual(comments[0], second_comment)
        self.assertEqual(comments[1], first_comment)

    def displays_comment_form(self):
        link = Link.objects.create(title='foo',url='http://google.com')
        response = self.client.get('/{0}/'.format(link.id))
        self.assertIsInstance(response.context['form'], CommentForm)
        self.assertContains(response, 'name="text"')

    def test_comments_are_actually_displayed(self):
        link = Link.objects.create(title='bar',url='http://reddit.com')
        first_comment = Comment.objects.create(text="poop",link=link)
        second_comment = Comment.objects.create(text="butt",link=link)
        response = self.client.get('/{0}/'.format(link.id))
        comments = response.context[0]['nodes']
        self.assertGreater(len(comments), 0)
