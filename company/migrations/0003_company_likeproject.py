# Generated by Django 3.2.5 on 2022-04-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('company', '0002_company_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='likeproject',
            field=models.ManyToManyField(to='project.Project', verbose_name='좋아요한 프로젝트'),
        ),
    ]
