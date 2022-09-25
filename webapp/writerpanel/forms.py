from django.forms import ModelForm
from django import forms
from website.models.makale import MakalelerModel
from website.models.yazi import YazilarModel
import os

# class CreatePostsForm(forms.ModelForm):
#     class Meta:
#         model = YazilarModel
#         fields =['resim','baslik','icerik','yazar']


class UpdatePostsForm(ModelForm):
    class Meta:
        model=YazilarModel
        fields=['resim','baslik','icerik']


class UpdateArticlesForm(ModelForm):
    class Meta:
        model=MakalelerModel
        fields=['baslik','makale',]

        

    # image = forms.FileField()

    # def clean_image(self):
    #     uploaded_file = self.cleaned_data['image']
    #     try:
    #         # create an ImageField instance
    #         im = forms.ImageField()
    #         # now check if the file is a valid image
    #         im.to_python(uploaded_file)
    #     except forms.ValidationError:
    #         # file is not a valid image;
    #         # so check if it's a pdf
    #         name, ext = os.path.splitext(uploaded_file.name)
    #         if ext not in ['.pdf', '.PDF']:
    #             raise forms.ValidationError("Only images and PDF files allowed")
    #     return uploaded_file
