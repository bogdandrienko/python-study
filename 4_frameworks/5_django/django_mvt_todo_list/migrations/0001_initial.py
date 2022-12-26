# Generated by Django 4.1.2 on 2022-10-28 03:40

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_column='title_db_column', db_index=True, db_tablespace='title_db_tablespace', default='', error_messages=False, help_text='<small class="text-muted">CharField [0, 300]</small><hr><br>', max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(300)], verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, db_column='description_db_column', db_index=True, db_tablespace='description_db_tablespace', default='', error_messages=False, help_text='<small class="text-muted">TextField [0, 3000]</small><hr><br>', max_length=3000, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(3000)], verbose_name='Описание')),
                ('is_completed', models.BooleanField(blank=True, db_column='is_completed_db_column', db_index=True, db_tablespace='is_completed_db_tablespace', default=False, error_messages=False, help_text='<small class="text-muted">BooleanField</small><hr><br>', verbose_name='Статус выполнения')),
                ('created', models.DateTimeField(blank=True, db_column='created_db_column', db_index=True, db_tablespace='created_db_tablespace', default=django.utils.timezone.now, error_messages=False, help_text='<small class="text-muted">DateTimeField</small><hr><br>', null=True, verbose_name='Дата и время создания')),
                ('updated', models.DateTimeField(blank=True, db_column='updated_db_column', db_index=True, db_tablespace='updated_db_tablespace', default=django.utils.timezone.now, error_messages=False, help_text='<small class="text-muted">DateTimeField</small><hr><br>', null=True, verbose_name='Дата и время обновления')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
                'db_table': 'django_mvt_todo_list_model_table',
                'ordering': ('-updated',),
            },
        ),
    ]
