# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 16:37
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_id', models.CharField(max_length=200)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
            ],
        ),
    ]
