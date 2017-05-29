from django import forms
from .models import Gallery


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        exclude = [
            'author',
            'created_at',
            'updated_at',
        ]