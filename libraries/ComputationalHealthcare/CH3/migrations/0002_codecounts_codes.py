# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-25 09:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CH3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeCounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('code_type', models.CharField(max_length=5)),
                ('count', models.IntegerField(default=0)),
                ('visit_type', models.IntegerField()),
                ('state', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('linked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('indexed', models.BooleanField(default=False)),
                ('total', models.IntegerField(default=0)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CH3.Datasets')),
            ],
        ),
    ]
