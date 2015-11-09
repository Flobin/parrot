from datetime import timedelta

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.utils import timezone

from posts.views import all_links
from posts.models import Link
from posts.forms import LinkForm

class HomePageTest(TestCase):

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'posts/all_links.html')

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

class SubmitViewTest(TestCase):

    def test_displays_link_form(self):
        response = self.client.get('/submit/')
        self.assertIsInstance(response.context['form'], LinkForm)
        self.assertContains(response, 'name="title"')

    def test_uses_submit_template(self):
        response = self.client.get('/submit/')
        self.assertTemplateUsed(response, 'posts/submit.html')
