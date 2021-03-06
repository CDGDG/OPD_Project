# Generated by Django 3.2.5 on 2022-04-01 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=20, verbose_name='개발자 아이디')),
                ('password', models.CharField(max_length=50, verbose_name='개발자 비밀번호')),
                ('nickname', models.CharField(max_length=15, verbose_name='닉네임')),
                ('registnum', models.CharField(max_length=13, verbose_name='주민번호')),
                ('phonenum', models.CharField(max_length=11, verbose_name='핸드폰 번호')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('regdate', models.DateTimeField(auto_now_add=True, verbose_name='등록일')),
                ('pic', models.FileField(null=True, upload_to='developer_pic/')),
                ('pic_original', models.TextField(default='')),
                ('resume', models.FileField(null=True, upload_to='developer_resume/')),
                ('resume_original', models.TextField(default='')),
                ('language', models.ManyToManyField(to='admin.Language')),
            ],
            options={
                'verbose_name': '개발자',
                'verbose_name_plural': '개발자(들)',
                'db_table': 'opd_developer',
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_follow_developer', to='developer.developer')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_follow_follower', to='developer.developer')),
            ],
            options={
                'verbose_name': '팔로우',
                'verbose_name_plural': '팔로우(들)',
                'db_table': 'opd_follow',
            },
        ),
    ]
