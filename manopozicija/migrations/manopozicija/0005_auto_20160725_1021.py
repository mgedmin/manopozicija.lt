# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-25 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manopozicija', '0004_auto_20160725_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
