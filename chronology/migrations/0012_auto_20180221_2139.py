# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0011_auto_20180221_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='interval',
            field=models.IntegerField(default=0, choices=[(0, '주간'), (1, '격주간'), (2, '월간'), (3, '1회성'), (4, '일간')]),
        ),
    ]
