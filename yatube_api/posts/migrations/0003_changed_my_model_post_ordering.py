# Generated by Django 2.2.16 on 2022-07-27 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_change_models_by_verbose_name_add_group_and_follow'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['pub_date'], 'verbose_name': 'Пост', 'verbose_name_plural': 'Посты'},
        ),
    ]
