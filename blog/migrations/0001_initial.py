# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=5)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'car',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('dept_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('dept_code', models.CharField(unique=True, max_length=5)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'dept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, b'\xe7\x94\xb7'), (2, b'\xe5\xa5\xb3'), (3, b'\xe5\x85\xb6\xe4\xbb\x96')])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'employee',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('engine_id', models.AutoField(serialize=False, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=5)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'engine',
                'managed': False,
            },
        ),
    ]
