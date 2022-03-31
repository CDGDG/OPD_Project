from django.shortcuts import render
from .models import Board
from django.core.paginator import Paginator
from .forms import Boardform
from developer.models import Developer

def board_list(request):
    boards_all = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1)) # 없으면 1로 지정
    paginator = Paginator(boards_all, 10)   # 한 페이지당 10개씩 보여준다
    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})

def board_create(request):
    if request.method == "POST":
        form = Boardform(request.POST)
        if form.is_valid():
            developer_id = request.session.get('developer')
            developer = Developer.objects.get(pk=developer_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.developer = developer
            board.save()
    

def board_detail(request, pk):
    pass

def board_update(request, pk):
    pass