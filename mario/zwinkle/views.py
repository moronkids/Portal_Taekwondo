from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from . models import konten, PostModel, krida_model, foto
from . forms import PostForm, krida_form
from allauth.account.forms import LoginForm
from django.contrib.auth.decorators import login_required
from .filters import kridafilter
from django import template

register = template.Library()

#---------- view foto -----

def fotoview(request):
    tampil = foto.objects.all()
    context = {
        'tampil':tampil
    }
    return render(request, 'base_post.html', context)


#------------

@login_required(redirect_field_name='account_login')
def tes(request):
    return render(request, 'tes.html')

@register.filter(name='superuser')
def home_post(request):
    PostTemp = PostModel.objects.all()
    tampil = foto.objects.all()
    print(PostTemp)
    context = {
        'page_title':'Krida Taekwondo News',
        'PostView':PostTemp,
        'tampil': tampil
    }
    return render(request, 'base_post.html', context)


def page(request):
    pageView = krida_model.objects.all()
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

def krida(request):
    user_list = krida_model.objects.filter(view__contains='ON').order_by('name')
    user_filter = kridafilter(request.GET, queryset=user_list)
    return render(request, 'krida/home_krida.html', {'filter': user_filter})

def hasilkrida(request):
    user_list = krida_model.objects.filter(hasilujian__contains='LULUS').order_by('hasilujian')
    user_filter = kridafilter(request.GET, queryset=user_list)
    return render(request, 'krida/nilai.html', {'filter': user_filter})

def administrasikrida(request):
    user_list = krida_model.objects.all()
    user_filter = kridafilter(request.GET, queryset=user_list)
    return render(request, 'krida/administrasi.html', {'filter': user_filter})

def about_krida(request):
    return render(request, 'krida/about.html')


def dojang(request):
    user_list = krida_model.objects.filter(view__contains='ON').order_by('dojang')
    user_filter = kridafilter(request.GET, queryset=user_list)
    return render(request, 'krida/dojang.html', {'filter': user_filter})


@login_required(redirect_field_name='krida')
def krida_create(request):
    kridadata = krida_form(request.POST or None)
    if request.method == 'POST':
        if kridadata.is_valid():
            kridadata.save()



        return redirect('reviews:dojang')
    context = {
        'page_title': 'Tambah Peserta',
        'kridadata':kridadata,
    }
    return render(request, 'post/posting_krida.html', context)

@login_required(redirect_field_name='deletekrida')
def deletekrida(request, delete_id_krida):
    krida_model.objects.filter(id=delete_id_krida).delete()
    return redirect('/blog/krida/')\

@login_required(redirect_field_name='deleteall')
def deleteall(request):
    krida_model.objects.all().delete()
    return redirect('/blog/krida/')

@login_required(redirect_field_name='updatekrida')
def updatekrida(request, update_id_krida):
    kridaupdate = krida_model.objects.get(id=update_id_krida)

    data = {
        'name'     : kridaupdate.name,
        'umur'       : kridaupdate.umur,
        'ttl'  : kridaupdate.ttl,
        'dojang'  : kridaupdate.dojang,
        'sabukawal'  : kridaupdate.sabukawal,
        'sabukujian'  : kridaupdate.sabukujian,
        'hasilujian'  : kridaupdate.hasilujian,
        'view'  : kridaupdate.view,

    }
    kridadata = krida_form(request.POST or None, initial=data, instance=kridaupdate)

    if request.method == 'POST':
        if kridadata.is_valid():
            kridadata.save()


        return redirect('reviews:dojang')
    context = {
        'page_title':'Update Peserta',
        'kridadata':kridadata,
    }
    return render(request, 'post/posting_krida.html', context)
