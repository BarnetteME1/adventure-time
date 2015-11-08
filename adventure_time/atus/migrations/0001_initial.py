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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('activity', models.CharField(max_length=82)),
                ('weight', models.FloatField()),
                ('minutesspend', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('caseid', models.CharField(max_length=14)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='household',
            name='caseid',
            field=models.ForeignKey(to='atus.Respondant'),
        ),
        migrations.AddField(
            model_name='activity',
            name='caseid',
            field=models.ForeignKey(to='atus.Respondant'),
        ),
    ]
