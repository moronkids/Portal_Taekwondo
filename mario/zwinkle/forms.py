from dal import autocomplete
from django import forms
from .models import PostModel, Collection, CollectionTitle, Anggota, Person, City, Ujian
from django.forms import inlineformset_factory, ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *
from gm2m import GM2MField
class PostForm(ModelForm):
    class Meta:
        model = PostModel
        fields = [
        'judul',
        'penulis',
        'gambar',
        'isi',
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




        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['gambar'].required = False


class CollectionTitleForm(forms.ModelForm):

    class Meta:
        model = Collection
        exclude = ()

CollectionTitleFormSet = inlineformset_factory(
    Anggota, Collection, form=CollectionTitleForm,
    fields=['id_reg', 'nama', 'tempat_lahir', 'tanggal_lahir', 'gambar',]
    , widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'class':'datepicker'}),

        }, extra=1, can_delete=True
    )


class AnggotaForm(forms.ModelForm):

    class Meta:
        model = Anggota
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(AnggotaForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-12'
        self.helper.layout = Layout(
            Div(
                Field('dojang'),
                Fieldset('Tambah Ujian',
                    Formset('titles')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
            )
            )


class CollectionForm(forms.ModelForm):

    class Meta:
        model = CollectionTitle
        exclude = ()

CollectionFormSet = inlineformset_factory(
    Ujian, CollectionTitle, form=CollectionForm,
    fields = ['sabukawal', 'sabukujian', 'hasilujian', 'waktu',], extra=1, can_delete=True
)

class UjianForm(forms.ModelForm):
    collection = forms.ModelChoiceField(
        queryset=Collection.objects.all(),widget=autocomplete.ModelSelect2(url='reviews:anggota-autocomplete'))
    print(collection)
    class Meta:
        model = Ujian
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(UjianForm, self).__init__(*args, **kwargs)
        self.fields['ujian_x'].widget.attrs['readonly'] = True
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-12'
        self.helper.layout = Layout(
            Div(
                Field('collection', name="tes"),
                HTML("<button  css_class='btn-info' type='button' id='cari'>Cari</button>"),
                HTML("<br>"),
                Field('ujian_x'),
                Fieldset('List Ujian'),
                    Formset('titles')),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
                )



