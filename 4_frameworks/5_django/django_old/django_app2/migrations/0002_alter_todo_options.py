# Generated by Django 4.1.2 on 2022-11-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('id',), 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
