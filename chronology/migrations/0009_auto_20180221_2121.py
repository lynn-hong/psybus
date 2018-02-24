# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0008_auto_20180221_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='part',
            options={'managed': True},
        ),
    ]
