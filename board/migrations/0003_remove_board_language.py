# Generated by Django 3.2.5 on 2022-04-01 06:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='language',
        ),
    ]