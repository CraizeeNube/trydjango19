from django import forms
from  .models import Post
from pagedown.widgets import PagedownWidget
from django.core.validators import *
from django.utils import timezone
from bootstrap_datepicker.widgets import DatePicker
from froala_editor.widgets import FroalaEditor
from datetimewidget.widgets import DateTimeWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor)
    draft = forms.BooleanField
    image = forms.FileField


    def clean_image(self):

        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 8 * 1024 * 1024:
                raise ValidationError("Image file too large ( > 4mb )")
            return image
        else:
            image =""
        return image


    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "image",
            'draft',
            'publish'

        ]
        widgets = {
            # Use localization and bootstrap 3
            'publish': DateTimeWidget(attrs={'id': "publish"}, usel10n=True, bootstrap_version=3)
        }