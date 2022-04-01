# Generated by Django 3.2.5 on 2022-04-01 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('developer', '0001_initial'),
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='프로젝트 타이틀')),
                ('summary', models.CharField(max_length=100, verbose_name='프로젝트 요약')),
                ('contents', models.TextField(verbose_name='프로젝트 내용')),
                ('startdate', models.DateTimeField(null=True)),
                ('enddate', models.DateTimeField(null=True)),
                ('viewcnt', models.IntegerField(default=0)),
                ('private', models.BooleanField(default=False)),
                ('thumbnail', models.FileField(upload_to='project_thumbnail/')),
                ('thumbnail_original', models.TextField()),
                ('language', models.ManyToManyField(to='admin.Language')),
                ('member', models.ManyToManyField(to='developer.Developer')),
            ],
            options={
                'verbose_name': '프로젝트',
                'verbose_name_plural': '프로젝트(들)',
                'db_table': 'opd_project',
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='project.project')),
                ('title', models.CharField(max_length=50, verbose_name='모집 타이틀')),
                ('contents', models.TextField(verbose_name='모집 내용')),
                ('regdate', models.DateTimeField(auto_now_add=True, verbose_name='모집 등록일')),
                ('viewcnt', models.IntegerField(default=0, verbose_name='조회수')),
                ('ing', models.BooleanField(default=False, verbose_name='모집 여부')),
            ],
            options={
                'verbose_name': '프로젝트 모집',
                'verbose_name_plural': '프로젝트 모집(들)',
                'db_table': 'opd_recruit',
            },
        ),
        migrations.CreateModel(
            name='RecruitOk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField()),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='developer.developer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
            options={
                'verbose_name': '프로젝트 모집처리',
                'verbose_name_plural': '프로젝트 모집(들)',
                'db_table': 'opd_recruitok',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='문서 카테고리')),
                ('docfile', models.FileField(upload_to='document_docfile/')),
                ('docfile_original', models.TextField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project', verbose_name='프로젝트')),
            ],
            options={
                'verbose_name': '프로젝트 문서',
                'verbose_name_plural': '프로젝트 문서(들)',
                'db_table': 'opd_document',
            },
        ),
        migrations.CreateModel(
            name='Recruit_Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.IntegerField()),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin.language')),
                ('recruit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project.recruit')),
            ],
            options={
                'verbose_name': '프로젝트 모집 언어',
                'verbose_name_plural': '프로젝트 모집 언어(들)',
                'db_table': 'opd_recruit_language',
            },
        ),
    ]
