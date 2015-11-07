# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from atus.atus_data import import_respondant


class Migration(migrations.Migration):

    dependencies = [
        ('atus', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_respondant)
    ]
