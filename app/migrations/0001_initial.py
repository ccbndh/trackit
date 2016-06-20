# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 04:32
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('slug_name', models.CharField(blank=True, max_length=500, null=True)),
                ('carrier_id', models.CharField(max_length=100, unique=True)),
                ('carrier_language', models.CharField(blank=True, max_length=100, null=True)),
                ('carrier_cs_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('carrier_url', models.CharField(blank=True, max_length=200, null=True)),
                ('carrier_url_tracking', models.CharField(blank=True, max_length=200, null=True)),
                ('carrier_logo', models.CharField(blank=True, max_length=100, null=True)),
                ('pattern_regex', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_event_type', models.CharField(max_length=500, null=True)),
                ('original_time', models.CharField(max_length=500, null=True)),
                ('original_location', models.CharField(max_length=500, null=True)),
                ('additional_params', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('carrier', models.ManyToManyField(to='app.Carrier')),
            ],
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_id', models.CharField(max_length=500, null=True)),
                ('picked_up_date', models.DateTimeField(blank=True, null=True)),
                ('delivered_date', models.DateTimeField(blank=True, null=True)),
                ('imported_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('origin_country', models.CharField(blank=True, max_length=500, null=True)),
                ('origin_locality', models.CharField(blank=True, max_length=500, null=True)),
                ('origin_raw_location', models.CharField(blank=True, max_length=500, null=True)),
                ('destination_country', models.CharField(blank=True, max_length=500, null=True)),
                ('destination_locality', models.CharField(blank=True, max_length=500, null=True)),
                ('destination_raw_location', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='parcel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Parcel'),
        ),
    ]
