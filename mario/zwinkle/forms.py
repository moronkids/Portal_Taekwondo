from django import forms
from .models import PostModel, krida_model
from django.forms import ModelForm


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


class krida_form(ModelForm):
    class Meta:

        model = krida_model
        fields = [

            'name',
            'umur',
            'penguji',
            'sabuk',
            'hasilujian',
            'pembayaran',
            'view',
        ]
        widgets = {
            'pembayaran': forms.Select(attrs={
                'class': 'forms-control',
                'choices': 'nominal',
            }),
            'hasilujian': forms.Select(attrs={
                'class': 'forms-control',
                'choices': 'hasil_ujian',
            }),
            'view': forms.Select(attrs={
                'class': 'forms-control',
                'choices': 'status',
            }),

        }
