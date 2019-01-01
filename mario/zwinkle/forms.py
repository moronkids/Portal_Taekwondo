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
        'penulis',
        'isi',
        'kategori',
        ]


        widgets = {
            'judul':forms.TextInput(attrs={
                'class':'form-control',

                'placeholder':'masukan judul'
            }),
            'penulis': forms.TextInput(attrs={
                'class': 'form-control',

                'placeholder': 'masukan penulis'
            }),
            'isi':forms.Textarea(attrs={

                'class': 'form-control',
                'placeholder': 'masukan isi'
            }),


            'kategori':forms.Select(attrs={

                'class': 'form-control',
                'choices':'CHOICES',
            }),
        }
