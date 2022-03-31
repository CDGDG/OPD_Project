from django.shortcuts import render
from .models import Developer
from .forms import JoinForm

def join(request):
    if request.method=="POST":
        form = JoinForm(request.POST)
    else:
        form = JoinForm()
    return render(request,'join.html',{'form':form})

def info(request):
    return render(request,'info.html')
def update(request):
    return render(request,'update.html')
def myproject(request):
    return render(request,'myproject.html')
def follow(request):
    return render(request,'follow.html')