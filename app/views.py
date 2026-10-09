from django.shortcuts import render
from django.contrib.auth.decorators import login_required




@login_required
def inicio(request):
    return render(request,"index.html")


@login_required
def profile(request):   
    return render(request,"profile.html")


@login_required
def config(request):
    return render(request,"configuration.html")