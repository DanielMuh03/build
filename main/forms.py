from datetime import datetime

from django import forms

from .models import Build, Image


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = ["title", "description", "build_time", "price", "category", "user"]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ("image",)


class UploadImageForm(forms.Form):
    image = forms.ImageField()


class UpdateBuildForm(forms.ModelForm):
    class Meta:
        model = Build
        fields = "__all__"
