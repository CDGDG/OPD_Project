<<<<<<< HEAD
# Generated by Django 3.2.5 on 2022-04-01 06:26
=======
# Generated by Django 3.2.5 on 2022-04-01 06:29
>>>>>>> fb3476a961e328be537e518163dc27a0e17e554d

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('project', '0002_auto_20220401_1526'),
        ('developer', '0003_remove_developer_language'),
        ('board', '0003_remove_board_language'),
        ('company', '0004_remove_company_language'),
=======
        ('project', '0002_auto_20220401_1529'),
        ('developer', '0003_remove_developer_language'),
        ('board', '0003_remove_board_language'),
        ('company', '0004_auto_20220401_1529'),
>>>>>>> fb3476a961e328be537e518163dc27a0e17e554d
        ('admin', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Language',
        ),
    ]
