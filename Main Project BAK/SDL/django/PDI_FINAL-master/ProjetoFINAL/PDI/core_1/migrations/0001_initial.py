# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Opencv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='opencv/media', verbose_name='Baixe a imagem:')),
            ],
        ),
    ]
