from django.http import HttpResponse, HttpResponseRedirect
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from . models import konten, PostModel, Krida_model, foto, Krida_model_detail
from zwinkle.forms import PostForm, krida_form, kridaformset, krida_formset
from allauth.account.forms import LoginForm
from django.contrib.auth.decorators import login_required
from .filters import kridafilter
from django import template
from django.shortcuts import render,redirect
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError

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

def krida(request):
    user_list = Krida_model.objects.filter(view__contains='ON').order_by('name')
    user_filter = kridafilter(request.GET, queryset=user_list)
    return render(request, 'krida/home_krida.html', {'filter': user_filter})

def hasilkrida(request):
    user_list = Krida_model.objects.filter(hasilujian__contains='LULUS').order_by('hasilujian')
    user_filter = kridafilter(request.GET, queryset=user_list)
    return render(request, 'krida/nilai.html', {'filter': user_filter})

def administrasikrida(request):
    context = {}
    user_list = Krida_model.objects.all()
    user_list_detail = Krida_model_detail.objects.all()
    context['admin']=user_list
    context['admin2']=user_list_detail
    return render(request, 'krida/administrasi.html', context )

def about_krida(request):
    return render(request, 'krida/about.html')


# def dojang(request):
#     objs = Krida_model.objects.all()
#     objs1 = Krida_model_detail.objects.all()
#     detail = krida
#     c = {
#         "brand_reports": objs,
#         "brand_reports1": objs1,
#     }
#     return render(request, "krida/dojang.html", c)

def dojang(request):
	datas = Krida_model_detail.objects.all()
	return render(request, 'krida/dojang.html', {'datas':datas})
# @login_required(redirect_field_name='krida')
# def krida_create(request):
#     context = {}
#     MarksFormset = modelformset_factory(Krida_model_detail, extra=1, form=krida_formset)
#     form = krida_form(request.POST or None)
#     formset = MarksFormset(request.POST or None, request.FILES or None, queryset=Krida_model_detail.objects.none(), prefix='taekwondo')
#     if request.method == "POST":
#         if form.is_valid() and formset.is_valid():
#             student = form.save(commit=False)
#             student.save()
#
#             for mark in formset:
#                 data = mark.save(commit=False)
#                 data.student = student
#                 data.save()
#
#             return redirect('reviews:blog')
#
#     context['form'] = krida_form()
#     context['formset'] = MarksFormset()
#
#     return render(request, 'post/posting_krida.html', context)

def krida_create(request):
    context = {}
    detailformset = modelformset_factory(Krida_model_detail, form=krida_formset)
    form = krida_form(request.POST or None, prefix='form')
    formset = detailformset(request.POST or None, queryset = Krida_model_detail.objects.none(), prefix='formset')
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            data = form.save(commit=False)
            data.save()
            obj_id = data.id
            for datas in formset:
                datasx = datas.save(commit=False)
                datasx.kridamodels.all = obj_id
                datasx.save()
    context['forms'] = form
    context['formset'] = formset

    return render(request, 'post/posting_krida.html', context)

# def krida_create(request):
#         context = {}
# 	    MarksFormset = modelformset_factory(Krida_model_detail, form=krida_formset)
# 	    form = krida_form(request.POST or None)
# 	    formset = MarksFormset(request.POST or None, queryset= Marks.objects.none(), prefix='marks')
# 	if request.method == "POST":
# 		if form.is_valid() and formset.is_valid():
# 			try:
# 				with transaction.atomic():
# 					student = form.save(commit=False)
# 					student.save()
#
# 					for mark in formset:
# 						data = mark.save(commit=False)
# 						data.student = student
# 						data.save()
#
#
#
#         context['formset'] = formset
#         context['form'] = form
#         return render(request, 'post/posting_krida.html', context)

@login_required(redirect_field_name='deletekrida')
def deletekrida(request, delete_id_krida):
    Krida_model.objects.filter(id=delete_id_krida).delete()
    return redirect('/blog/krida/')

@login_required(redirect_field_name='deleteall')
def deleteall(request):
    Krida_model.objects.all().delete()
    #Krida_model_detail.objects.all().delete()
    return redirect('/blog/krida/')

@login_required(redirect_field_name='updatekrida')
def updatekrida(request, update_id_krida):
    context = {}
    detailformset = modelformset_factory(Krida_model_detail, form=krida_formset)
    form = krida_form(request.POST or None)
    formset = detailformset(request.POST or None, queryset=Krida_model_detail.objects.none(),
                            prefix='krida_model_detail')
    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                krida = form.save(commit=False)
                krida.save()

                for data in formset:
                    detail = data.save(commit=False)
                    detail.save()
    context['forms'] = form
    context['formset'] = formset

    return render(request, 'post/posting_krida.html', context)
    # kridaupdate = Krida_model.objects.get(id=update_id_krida)
    #
    # data = {
    #     'name'     : kridaupdate.name,
    #     'umur'       : kridaupdate.umur,
    #     'ttl'  : kridaupdate.ttl,
    #     'dojang'  : kridaupdate.dojang,
    #     'view'  : kridaupdate.view,
    #
    # }
    # kridadata = krida_form(request.POST or None, initial=data, instance=kridaupdate)
    #
    # if request.method == 'POST':
    #     if kridadata.is_valid():
    #         kridadata.save()
    #
    #
    #     return redirect('reviews:dojang')
    # context = {
    #     'page_title':'Update Peserta',
    #     'kridadata':kridadata,
    # }
    # return render(request, 'post/posting_krida.html', context)
