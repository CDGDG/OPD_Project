from django.db import models
from project.models import Project, Language

class Developer(models.Model):
    userid = models.CharField(max_length=20, verbose_name ='개발자 아이디')
    password = models.CharField(max_length=50, verbose_name='개발자 비밀번호')
    nickname = models.CharField(max_length=15,verbose_name='닉네임')
    regisnum = models.CharField(max_length=13,verbose_name = '주민번호')
    phonenum = models.CharField(max_length=11,verbose_name='핸드폰 번호')
    email = models.EmailField(max_length=128,verbose_name='이메일')
    regdate = models.DateTimeField(auto_now_add=True,verbose_name='등록일')
    pic = models.FileField(upload_to='developer_pic/')
    pic_original = models.TextField(null=False)
    resume = models.FileField(upload_to = 'developer_resume/')
    resume_original = models.TextField(null=False)

    language = models.ManyToManyField(Language)
    likeproject = models.ManyToManyField(Project)

    class Meta:
        db_table = 'opd_developer'
        verbose_name = '개발자'
        verbose_name_plural = '개발자(들)'


    def __str__(self):
        return self.userid

class Follow(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE,related_name='%(class)s_follow_developer')
    follower = models.ForeignKey(Developer,on_delete=models.CASCADE,related_name='%(class)s_follow_follower')

    class Meta:
        db_table='opd_follow'
        verbose_name='팔로우'
        verbose_name_plural = '팔로우(들)'

    def __str__(self):
        return self.developer


