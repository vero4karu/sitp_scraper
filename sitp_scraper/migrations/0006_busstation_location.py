# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-04 21:21
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitp_scraper', '0005_busstation_location_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='busstation',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
