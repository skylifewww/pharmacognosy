# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-03 21:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_author_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['article_date'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]
