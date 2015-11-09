from django import forms
from django.forms import ModelForm
from .models import Link

TITLE_LENGTH_ERROR = "This title is too long, please make it 140 characters or less."
TITLE_EMPTY_ERROR = "You’ll have to add a title"
URL_EMPTY_ERROR = "Please enter a valid URL"

class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['title', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a descriptive title'}),
            'url': forms.TextInput(attrs={'placeholder': 'The link'}),
        }
        error_messages = {
            'title': {
                'max_length': TITLE_LENGTH_ERROR,
                'required': TITLE_EMPTY_ERROR,
            },
            'url': {
                'required': URL_EMPTY_ERROR,
            }
        }
