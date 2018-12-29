from django import forms
from .models import PostModel
from django.forms import ModelForm

#class PostForm(forms.Form):
 #   judul = forms.CharField(max_length=100)
  #  isi = forms.CharField(max_length=100)
   # kategori = forms.CharField(max_length=100)

class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = [
        'judul',
        'isi',
        'kategori',
        ]