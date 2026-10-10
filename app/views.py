from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post



@login_required
def inicio(request):

    posts = Post.objects.all().order_by("criado_em")

    dados = {

        "posts" : posts

    }


    return render(request,"index.html",dados)


@login_required
def profile(request):   
    return render(request,"profile.html")


@login_required
def config(request):
    return render(request,"configuration.html")