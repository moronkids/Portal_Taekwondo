from django.http import HttpResponse
from django.shortcuts import render
from . models import konten
from django.contrib.auth.decorators import login_required

def home(request):

    return render(request, 'index.html')

@login_required(redirect_field_name='login')
def tes(request):
    return render(request, 'tes.html')
