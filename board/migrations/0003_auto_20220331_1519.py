# Generated by Django 3.2.5 on 2022-03-31 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('board', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.language', verbose_name='언어'),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='opd_comment',
        ),
    ]