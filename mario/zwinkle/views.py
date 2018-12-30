from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from . models import konten, PostModel
from . forms import PostForm
from allauth.account.forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required(redirect_field_name='account_login')
def tes(request):
    return render(request, 'tes.html')

@login_required(redirect_field_name='blog')
def home_post(request):
    PostTemp = PostModel.objects.all()
    print(PostTemp)
    context = {
        'page_title':'CRUD Django 2.1',
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