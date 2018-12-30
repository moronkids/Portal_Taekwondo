from django import forms
from .models import PostModel
from django.forms import ModelForm, Textarea, CharField

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

        widgets = {
            'judul':Textarea(attrs={'cols':30, 'rows':1, 'placeholder':'masukan judul'}),
            'isi':Textarea(attrs={'cols':75, 'rows':10}),
            'kategori':Textarea(attrs={'cols':30, 'rows':1}),
        }