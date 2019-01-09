from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from . models import konten, PostModel, krida_model
from . forms import PostForm, krida_form
from rest_framework import generics
from allauth.account.forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='account_login')
def tes(request):
    return render(request, 'tes.html')


def home_post(request):
    PostTemp = PostModel.objects.all()
    print(PostTemp)
    context = {
        'page_title':'Post List Detail',
        'PostView':PostTemp,
    }
    return render(request, 'base_post.html', context)
#def create(request):

@login_required(redirect_field_name='create')
def create(request):
    PostData = PostForm(request.POST or None)
    if request.method == 'POST':
        if PostData.is_valid():
            PostData.save()

        return redirect('reviews:blog')
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
    kridatemp = krida_model.objects.all()
    print(kridatemp)
    context = {
        'page_title':'Post List Detail',
        'kridaView':kridatemp,
    }
    return render(request, 'base_krida.html', context)

@login_required(redirect_field_name='krida')
def krida_create(request):
    kridadata = krida_form(request.POST or None)
    if request.method == 'POST':
        if kridadata.is_valid():
            kridadata.save()

        return redirect('reviews:krida')
    context = {
        'page_title': 'Create Post Krida',
        'kridadata':kridadata,
    }
    return render(request, 'post/posting_krida.html', context)

@login_required(redirect_field_name='deletekrida')
def deletekrida(request, delete_id_krida):
    krida_model.objects.filter(id=delete_id_krida).delete()
    return redirect('/blog/krida/')

@login_required(redirect_field_name='updatekrida')
def updatekrida(request, update_id_krida):
    kridaupdate = krida_model.objects.get(id=update_id_krida)

    data = {
        'nama'     : kridaupdate.nama,
        'umur'       : kridaupdate.umur,
        'penguji'  : kridaupdate.penguji,
        'sabuk'  : kridaupdate.sabuk,

    }
    kridadata = krida_form(request.POST or None, initial=data, instance=kridaupdate)
    if request.method == 'POST':
        if kridadata.is_valid():
            kridadata.save()

        return redirect('reviews:krida')
    context = {
        'page_title':'Update Post',
        'kridadata':kridadata,
    }
    return render(request, 'post/posting_krida.html', context)