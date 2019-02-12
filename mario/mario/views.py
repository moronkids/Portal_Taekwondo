from django.shortcuts import render, redirect

def home(request):

    return render(request, 'landing_page/index_isi.html')