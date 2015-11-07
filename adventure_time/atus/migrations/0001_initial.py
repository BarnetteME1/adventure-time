# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('code', models.IntegerField()),
                ('weight', models.FloatField()),
                ('activity', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('minutesspend', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('location', models.IntegerField()),
                ('houseincome', models.IntegerField()),
                ('ownorrent', models.IntegerField()),
                ('numberinhouse', models.IntegerField()),
                ('highesteducation', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Respondant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('caseid', models.CharField(max_length=14)),
                ('peronlinenumber', models.IntegerField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
    ]
