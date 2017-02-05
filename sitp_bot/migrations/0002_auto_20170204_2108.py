# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-05 02:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitp_bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='botuser',
            options={'ordering': ['-updated_at'], 'verbose_name': 'Bot User', 'verbose_name_plural': 'Bot Users'},
        ),
        migrations.AlterModelOptions(
            name='botuserrequeststats',
            options={'ordering': ['-day', '-requests_count'], 'verbose_name': 'Bot User stats', 'verbose_name_plural': 'Bot User stats'},
        ),
        migrations.AlterModelOptions(
            name='messagestats',
            options={'ordering': ['-requests_count'], 'verbose_name': 'Bot Messages Stats', 'verbose_name_plural': 'Bot Messages Stats'},
        ),
        migrations.AddField(
            model_name='botuser',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
