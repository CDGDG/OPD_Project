from django.db import models

from developer.models import Developer


class Board(models.Modle):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, verbose_name='개발자')
    language = models.IntegerField(default=0, verbose_name='언어')
    title = models.CharField(max_length=20, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    regdate = models.DateField(auto_now_add=True, verbose_name='등록시간')
    viewcnt = models.IntegerField(default=0, verbose_name='조회수')

    class Meta:
        db_table = 'opd_board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판(들)'

class Boardimg(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, primary_key=True, verbose_name='게시판')
    boardimg = models.TextField(verbose_name='게시판그림')
    img_original = models.CharField(null=False)

    class Meta:
        db_table = 'opd_boardimg'
        verbose_name = '게시판그림'
        verbose_name_plural = '게시판그림(들)'
    

