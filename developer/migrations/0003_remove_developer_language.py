<<<<<<< HEAD
# Generated by Django 3.2.5 on 2022-04-01 06:26
=======
# Generated by Django 3.2.5 on 2022-04-01 06:29
>>>>>>> fb3476a961e328be537e518163dc27a0e17e554d

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0002_developer_likeproject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='developer',
            name='language',
        ),
    ]
