# Generated by Django 3.2.5 on 2022-04-01 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyid', models.CharField(max_length=20, verbose_name='회사아이디')),
                ('password', models.CharField(max_length=50, verbose_name='회사비밀번호')),
                ('name', models.CharField(max_length=15, verbose_name='회사이름')),
                ('pic', models.FileField(upload_to='company_pic/', verbose_name='회사프로필사진')),
                ('pic_original', models.CharField(max_length=200, verbose_name='회사프로필사진이름')),
                ('tel', models.CharField(max_length=11, verbose_name='회사전화번호')),
                ('email', models.EmailField(max_length=128, verbose_name='회사이메일')),
                ('address', models.CharField(max_length=30, verbose_name='회사주소')),
                ('summary', models.TextField(verbose_name='회사설명')),
                ('regdate', models.DateTimeField(auto_now_add=True, verbose_name='가입시간')),
                ('url', models.TextField(verbose_name='회사홈페이지URL')),
                ('people', models.PositiveIntegerField(verbose_name='직원수')),
                ('category', models.CharField(max_length=10, verbose_name='분류')),
                ('language', models.ManyToManyField(to='project.Language', verbose_name='사용언어')),
                ('likeproject', models.ManyToManyField(to='project.Project', verbose_name='좋아요한 프로젝트')),
            ],
            options={
                'verbose_name': '회사',
                'verbose_name_plural': '회사(들)',
                'db_table': 'opd_company',
            },
        ),
    ]
