from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Project
from .forms import Projectform

def list(request):
    all_projects = Project.objects.all().order_by('-id')

    # 페이징
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_projects, 5) # 한 페이지당 5개씩 보여주는 Paginator 생성
    projects = paginator.get_page(page)

    return render(request, 'project_list.html', {"projects": projects})

def create(request):
    
    form = Projectform()
    return render(request, 'project_create.html', {'form': form})
