from django.test import TestCase
from django.core.exceptions import ValidationError

from posts.models import Link

class ListAndItemModelsTest(TestCase):

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
