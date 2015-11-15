from django.test import TestCase

from posts.models import Link, Comment
from posts.forms import (
    LinkForm,
    TITLE_LENGTH_ERROR,
    TITLE_EMPTY_ERROR,
    URL_EMPTY_ERROR,
    CommentForm,
    TEXT_EMPTY_ERROR,
)


class LinkFormTest(TestCase):

    def test_form_item_input_has_placeholder(self):
        form = LinkForm()
        self.assertIn('placeholder="Enter a descriptive title"', form.as_p())

    def test_form_validation_for_blank_titles_and_urls(self):
        form = LinkForm(data={'title': '', 'url': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['title'],
            [TITLE_EMPTY_ERROR]
        )
        self.assertEqual(
            form.errors['url'],
            [URL_EMPTY_ERROR]
        )

    def test_form_validation_for_too_long_titles(self):
        form = LinkForm(data={'title': 'An unexpected failure—it’s actually in the tests for our final view, view_list. Because we’ve changed the way errors are displayed in all templates, we’re no longer showing the error that we manually pass into the template.', 'url': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['title'],
            [TITLE_LENGTH_ERROR]
        )

    def test_form_saves(self):
        #link = Link.objects.create()
        form = LinkForm(data={'title': 'poop', 'url': 'http://google.com/'})
        form.save()
        self.assertEqual(Link.objects.all().count(), 1)

class CommentFormTest(TestCase):

    def test_form_validation_for_empty_textarea(self):
        form = CommentForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['text'],
            [TEXT_EMPTY_ERROR]
        )
