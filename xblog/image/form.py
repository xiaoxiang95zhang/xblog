from django import forms
from django.core.files.base import ContentFile
from slugify import slugify
#from urllib import requeste
import urllib

from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError("the give url do not match")
        return url

    def save(self, force_insert=False, force_updata=False, commit=True):
        image = super(ImageForm, self).save(commit=False)
        image_url = self.cleaned_data["url"]
        image_name = '{0}.{1}'.format(slugify(image.title),
            image_url.rsplit('.', 1)[1].lower())
        response = urllib.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        if commit:
            image.save()

        return image