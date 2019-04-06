from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from . models import konten, PostModel, Collection, foto, CollectionTitle
from zwinkle.forms import PostForm, CollectionForm, CollectionTitleFormSet
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
register = template.Library()

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

    paginator = Paginator(user_list, 4)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
       'page_title':'Krida Taekwondo News',
        'users':users
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

def about_krida(request):
    return render(request, 'krida/about.html')


# ----------- baru krida ---------------

class HomepageView(TemplateView):
    template_name = "mycollections/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.order_by('id')
        return context

class Ujian(TemplateView):
    template_name = "mycollections/collection_ujian.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.filter(has_titles__hasilujian__contains="-", ).order_by('-id')
        context['x']=CollectionTitle.objects.all().order_by('-hasilujian')
        return context


##########################################################################
#                           Collection views                             #
##########################################################################

class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'mycollections/collection_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        return context

class CollectionCreate(CreateView):
    model = Collection
    template_name = 'mycollections/collection_create.html'
    form_class = CollectionForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(CollectionCreate, self).get_context_data(**kwargs)
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
        return super(CollectionCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('reviews:collection_detail', kwargs={'pk': self.object.pk})


    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionCreate, self).dispatch(*args, **kwargs)


class CollectionUpdate(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'mycollections/collection_create.html'

    def get_context_data(self, **kwargs):
        data = super(CollectionUpdate, self).get_context_data(**kwargs)
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
        return super(CollectionUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('reviews:collection_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(CollectionUpdate, self).dispatch(*args, **kwargs)


class CollectionDelete(DeleteView):
    model = Collection
    template_name = 'mycollections/confirm_delete.html'
    success_url = reverse_lazy('reviews:homepage')