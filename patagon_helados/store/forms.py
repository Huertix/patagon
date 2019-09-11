from django import forms
from django.forms import Textarea

from store.models import Image, Text


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["name", "imagefile"]


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ["name",  "language"]
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
