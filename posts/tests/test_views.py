from datetime import timedelta

from unittest import skip

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.utils import timezone
from django.contrib.auth.models import User

from posts.views import links, comments
from posts.models import Link, Comment
from posts.forms import LinkForm

class HomePageTest(TestCase):

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

class CommentsViewTest(TestCase):

    def test_comments_view_renders_comments_template(self):
        link = Link.objects.create(title='foo',url='http://google.com')
        response = self.client.get('/{0}/'.format(link.id))
        self.assertTemplateUsed(response, 'posts/comments.html')

    @skip("chronology isn't really important anyway...")
    def test_comments_are_displayed_chronologically(self):
        link = Link.objects.create(title='bar',url='http://reddit.com',posted=timezone.now()-timedelta(days=1))
        first_comment = Comment.objects.create(text="poop",content_object=link)
        second_comment = Comment.objects.create(text="butt",content_object=link,posted=timezone.now()-timedelta(days=2))
        response = self.client.get('/{0}/'.format(link.id))
        comments = response.context[0]['comments']
        self.assertEqual(comments[0], second_comment)
        self.assertEqual(comments[1], first_comment)

class SubmitViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')

    def test_displays_link_form(self):
        response = self.client.get('/submit/')
        self.assertIsInstance(response.context['form'], LinkForm)
        self.assertContains(response, 'name="title"')

    def test_uses_submit_template(self):
        response = self.client.get('/submit/')
        self.assertTemplateUsed(response, 'posts/submit.html')
