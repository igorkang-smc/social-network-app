import uuid

import requests
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'url', 'description']
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.'
            )
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from the given URL
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/115.0 Safari/537.36"
        }
        response = requests.get(image_url, headers=headers)
        image.image.save(
            image_name,
            ContentFile(response.content),
            save=False
        )
        if commit:
            image.save()
        return image


class ImageCreateManualForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'description', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            valid_extensions = ['jpg', 'jpeg', 'png']
            extension = image.name.rsplit('.', 1)[1].lower()
            if extension not in valid_extensions:
                raise forms.ValidationError(
                    'The uploaded file is not a valid image format (jpg, jpeg, png).'
                )
        return image

    def save(self, commit=True):
        image = super().save(commit=False)
        if image.image:
            name = slugify(image.title)
            extension = image.image.name.rsplit('.', 1)[1].lower()
            unique_suffix = uuid.uuid4().hex[:8]  # короткий уникальный хэш
            image.image.name = f"{name}-{unique_suffix}.{extension}"
        if commit:
            image.save()
        return image