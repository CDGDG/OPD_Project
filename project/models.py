from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name='프로젝트 타이틀')
    summary = models.CharField(max_length=100, verbose_name='프로젝트 요약')
    contents = models.TextField(verbose_name='프로젝트 내용')
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    viewcnt = models.IntegerField(default=0)
    private = models.BooleanField(default=False)
    # thumbnail = models.
