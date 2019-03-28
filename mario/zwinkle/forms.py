from django import forms
from .models import PostModel, Krida_model, Krida_model_detail
from django.forms import formset_factory, ModelForm



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
        model = Krida_model
        fields = [
            'name',
            'ttl',
            'dojang',
            'umur',
            'view',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control','id':'name', 'label':'nama'
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

        }

class krida_formset(ModelForm):
    class Meta:
        model = Krida_model_detail
        fields = [
            'sabukawal',
            'sabukujian',
            'hasilujian',
            'waktu',
        ]
        widgets = {
            'sabukawal': forms.Select(attrs={
                'id':'sabukawal',
                'class': 'formset-field',
                'choices': 'sabukawal',
            }),
            'sabukujian': forms.Select(attrs={
                'id': 'sabukujian',
                'class': 'formset-field',
                'choices': 'sabukujian',
            }),
            'hasilujian': forms.Select(attrs={
                'class': 'formset-field',
                'choices': 'hasil_ujian',
                'id': 'hasilujian'
            }),
        }

kridaformset = formset_factory(krida_formset, extra=15)