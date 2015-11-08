# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from atus.atus_data import import_household


class Migration(migrations.Migration):

    dependencies = [
        ('atus', '0003_auto_20151107_2158'),
    ]

    operations = [
        migrations.RunPython(import_household)
    ]
