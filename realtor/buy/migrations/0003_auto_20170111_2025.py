# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_buy_overview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buy',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='buy',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]