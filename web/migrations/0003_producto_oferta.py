# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20170414_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='oferta',
            field=models.BooleanField(default=False, verbose_name='Oferta'),
        ),
    ]
