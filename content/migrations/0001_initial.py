# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-29 13:59
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.CharField(blank=True, max_length=250, verbose_name='Урл')),
                ('full_text', ckeditor.fields.RichTextField(blank=True, verbose_name='Полное описание')),
                ('published', models.BooleanField(verbose_name='Опубликован')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Порядок сортировки')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='content.Menu', verbose_name='Меню')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='content.MenuItem', verbose_name='Родительский пункт меню')),
            ],
            options={
                'verbose_name_plural': 'Пункты меню',
            },
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_description', ckeditor.fields.RichTextField(blank=True, verbose_name='Мета описание')),
                ('meta_keywords', models.CharField(blank=True, max_length=250, verbose_name='Ключевые слова')),
                ('meta_title', models.CharField(blank=True, max_length=250, verbose_name='Заголовок в браузере')),
                ('meta_author', models.CharField(blank=True, max_length=250, verbose_name='Автор сайта')),
                ('favicon_slug', models.CharField(blank=True, max_length=250, verbose_name='Урл favicon')),
                ('published', models.BooleanField(default=0, verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Мета описание',
                'verbose_name_plural': 'Мета описания',
            },
        ),
        migrations.CreateModel(
            name='Snipet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(blank=True, verbose_name='Код снипета')),
                ('published', models.BooleanField(verbose_name='Опубликован')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Порядок сортировки')),
            ],
            options={
                'verbose_name': 'Сниппет',
                'verbose_name_plural': 'Сниппеты',
            },
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(blank=True, max_length=250, verbose_name='Урл')),
                ('text_small', models.CharField(blank=True, max_length=250, verbose_name='Обещание')),
                ('text_big', models.CharField(blank=True, max_length=250, verbose_name='Заявка на победу')),
                ('published', models.BooleanField(verbose_name='Опубликован')),
            ],
            options={
                'verbose_name': 'Шапка',
                'verbose_name_plural': 'Шапки',
            },
        ),
    ]
