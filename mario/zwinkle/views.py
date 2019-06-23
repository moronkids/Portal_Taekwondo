from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from . models import konten, PostModel, Collection, foto, CollectionTitle, Anggota, Person, City, Ujian
from zwinkle.forms import PostForm, AnggotaForm, CollectionTitleFormSet, CollectionForm, CollectionFormSet, UjianForm
from allauth.account.forms import LoginForm
from django.contrib.auth.decorators import login_required
from .filters import kridafilter
from django import template
from django.shortcuts import render,redirect
from django.forms import modelformset_factory, inlineformset_factory
from django.db import transaction, IntegrityError
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from urllib import request
from django.contrib import messages
register = template.Library()
from dal import autocomplete
from dal_select2_queryset_sequence.views import Select2QuerySetSequenceView
from django.db.models import Q
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
import  json
# from .models import TestModel


class IndexView(TemplateView):
    template_name = 'index2.html'

class TestModelList(TemplateView):
    model = CollectionTitle
    template_name = 'testmodel_list.html'
    # daya
    def get_context_data(self, **kwargs):
        context = super(TestModelList, self).get_context_data(**kwargs)
        # context['history'] = CollectionTitle.objects.all()
        return context


class TestModelListJson(BaseDatatableView):
    model = CollectionTitle
    # datatable_options = {
    #     'columns': [
    #         'namax',
    #         ("hasilujian", 'has_titles__hasilujian'),
    #     ],
    # }

    # columns and order columns are provided by datatables in the request using "name" in columns definition
# class LocationAutocompleteView(Select2QuerySetSequenceView):
#     def get_queryset(self):
#         dojang = Anggota.objects.all()
#         peserta = Collection.objects.all()
#
#         if self.q:
#             dojang = Anggota.filter(dojang__icontains=self.q)
#             peserta = Collection.filter(anggota_uti__nama__icontains=self.q)
#
#         # Aggregate querysets
#         qs = QuerySetSequence(dojang, peserta)
#
#         if self.q:
#             # This would apply the filter on all the querysets
#             qs = qs.filter(nama__icontains=self.q)
#
#         # This will limit each queryset so that they show an equal number
#         # of results.
#         qs = self.mixup_querysets(qs)
#
#         return qs

class AnggotaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Collection.objects.exclude(has_titles__hasilujian__icontains=False)

        if self.q:
            qs = qs.filter(nama__istartswith=self.q)

        return qs


#---------- view foto -----

def fotoview(request):
    tampil = foto.objects.all()

    context = {
        'tampil':Paginator
    }
    return render(request, 'base_post.html', context)


#------------

@login_required(redirect_field_name='account_login')
def tes(request):
    return render(request, 'tes.html')



@register.filter(name='superuser')
def home_post(request):
    user_list = PostModel.objects.all()
    page = request.GET.get('page', 1)
    # user_filterx = postfilter(request.GET, queryset=user_list)
    paginator = Paginator(user_list, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
       'page_title':'Krida Taekwondo News',
        'users':users,
        # 'filter':user_filterx
    }
    return render(request, 'base_post.html', context)
# def home_post(request):
#     PostTemp = PostModel.objects.all()
#     tampil = foto.objects.all()
#     Paginator = Paginator(tampil, 10)
#     print(PostTemp)
#     context = {
#         'page_title':'Krida Taekwondo News',
#         'PostView':PostTemp,
#         'tampil': Paginator
#     }
#     return render(request, 'base_post.html', context)


def page(request):
    pageView = Krida_model.objects.all()
    context = {
        'page_title':'Krida Taekwondo News',
        'pageView':pageView,
    }
    return render(request, 'tes/page.html', context)

def create(request):
    if request.method == 'POST':
        PostData = PostForm(request.POST, request.FILES or None)
        if PostData.is_valid():
            PostData.save()
            return redirect('reviews:blog')
    else:
        PostData = PostForm()
    context = {
        'page_title': 'Create Post',
        'PostData':PostData,
    }
    return render(request, 'post/posting.html', context)

def about(request):
    return render(request, 'krida/about.html')

@login_required(redirect_field_name='delete')
def delete(request, delete_id):
    PostModel.objects.filter(id=delete_id).delete()
    return redirect('/blog')

@login_required(redirect_field_name='update')
def update(request, update_id):
    PostUpdate = PostModel.objects.get(id=update_id)

    data = {
        'judul'     : PostUpdate.judul,
        'isi'       : PostUpdate.isi,
        'kategori'  : PostUpdate.kategori,

    }
    PostData = PostForm(request.POST or None, initial=data, instance=PostUpdate)
    if request.method == 'POST':
        PostData = PostForm(request.POST or None, request.FILES, initial=data, instance=PostUpdate)
        if PostData.is_valid():
            PostData.save()

        return redirect('reviews:blog')

    context = {
        'page_title':'Update Post',
        'PostData':PostData,
    }
    return render(request, 'post/posting.html', context)

# -------------------------------------------------------------------------------

# ----------- baru krida ---------------

def base(request):
    nama_list = Collection.objects.all().order_by('nama')
    user_filter = kridafilter(request.GET, queryset=nama_list)
    return render(request, 'mycollections/base.html', {'filter': user_filter})


def ujian(request):
    user_list = Collection.objects.filter(daftar__ujian_x__icontains="BELUM UJIAN").order_by('id')
    user_filter = kridafilter(request.GET, queryset=user_list)
    return render(request, 'mycollections/collection_ujian.html', {'filter': user_filter})

def nilai(request):
    user_list = Collection.objects.filter(daftar__ujian_x__icontains="SUDAH UJIAN")
    user_filter = kridafilter(request.GET, queryset=user_list)
    return render(request, 'krida/nilai.html', {'filter': user_filter})

##########################################################################
#                           Collection views                             #
##########################################################################

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'mycollections/anggota_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        context['history'] = CollectionTitle.objects.all()
        return context

class AnggotaCreate(CreateView):
    model = Anggota
    template_name = 'mycollections/anggota_create.html'
    form_class = AnggotaForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(AnggotaCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CollectionTitleFormSet(self.request.POST, self.request.FILES or None)
        else:
            data['titles'] = CollectionTitleFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(AnggotaCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('reviews:collection_detail', kwargs={'pk': self.object.pk})

class CollectionCreate(CreateView):
    model = Ujian
    template_name = 'mycollections/collection_create.html'
    form_class = UjianForm
    success_url = None


    def get_context_data(self, **kwargs):
        data = super(CollectionCreate, self).get_context_data(**kwargs)
        data['masuk'] = Collection.objects.all()
        if self.request.POST:
            data['titles'] = CollectionFormSet(self.request.POST, self.request.FILES or None)
        else:
            data['titles'] = CollectionFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionCreate, self).form_valid(form)

class CollectionHistory(CreateView):
    model = Ujian
    template_name = 'mycollections/collection_create.html'
    form_class = UjianForm
    success_url = None


    def get_context_data(self, **kwargs):
        data = super(CollectionHistory, self).get_context_data(**kwargs)
        data['masuk'] = Collection.objects.all()
        if self.request.POST:
            data['titles'] = CollectionFormSet(self.request.POST, self.request.FILES or None)
        else:
            data['titles'] = CollectionFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionHistory, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('reviews:anggota_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionCreate, self).dispatch(*args, **kwargs)


class CollectionUpdate(UpdateView):
    model = Ujian
    template_name = 'mycollections/collection_create.html'
    form_class = UjianForm

    def get_context_data(self, **kwargs):
        data = super(CollectionUpdate, self).get_context_data(**kwargs)

        if self.request.POST:
            data['titles'] = CollectionFormSet(self.request.POST, instance=self.object)
        else:
            data['titles'] = CollectionFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(CollectionUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('reviews:collection_detail', kwargs={'pk': self.object.pk})

class AnggotaUpdate(UpdateView):
    model = Anggota
    form_class = AnggotaForm
    template_name = 'mycollections/anggota_create.html'

    def get_context_data(self, **kwargs):
        data = super(AnggotaUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CollectionTitleFormSet(self.request.POST, instance=self.object)
        else:
            data['titles'] = CollectionTitleFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
        return super(AnggotaUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('reviews:anggota_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
#     #     return super(CollectionUpdate, self).dispatch(*args, **kwargs)


class CollectionDelete(DeleteView):
    model = Ujian
    template_name = 'mycollections/confirm_delete.html'
    success_url = reverse_lazy('reviews:homepage')

class AnggotaDelete(DeleteView):
    model = Collection
    template_name = 'mycollections/confirm_delete.html'
    success_url = reverse_lazy('reviews:homepage')


