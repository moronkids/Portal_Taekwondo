from django import forms
from .models import PostModel, krida_model
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = [
        'judul',
        'penulis',
        'gambar',
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

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['gambar'].required = False


class krida_form(ModelForm):
    class Meta:

        model = krida_model
        fields = [

            'name',
            'ttl',
            'dojang',
            'umur',
            'sabukawal',
            'sabukujian',
            'hasilujian',
            'view',
            'waktu',

        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control','id':'name', 'label':'nama'
            }),

            'waktu': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'waktu', 'label': 'waktu'
            }),

            'ttl': forms.TextInput(attrs={
                'class':'form-control','id':'ttl'
            }),
            'dojang': forms.Select(attrs={
                'class':'form-control','id':'dojang',
                'choices':'dojang'
            }),
            'umur': forms.TextInput(attrs={
                'class':'form-control','id':'umur'
            }),


            'sabukawal': forms.Select(attrs={
                'id':'sabukawal',
                'class': 'form-control',
                'choices': 'sabukawal',
            }),
            'sabukujian': forms.Select(attrs={
                'id': 'sabukujian',
                'class': 'form-control',
                'choices': 'sabukujian',
            }),
            'hasilujian': forms.Select(attrs={
                'class': 'form-control',
                'choices': 'hasil_ujian',
                'id': 'hasilujian'
            }),
            'view': forms.Select(attrs={
                'class': 'form-control',
                'choices': 'status',
                'id': 'view'
            }),

        }