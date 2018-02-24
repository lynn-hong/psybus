# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0013_auto_20180221_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='interval',
            field=models.IntegerField(choices=[(0, '주간'), (1, '격주간'), (2, '월간'), (3, '1회성'), (4, '일간'), (5, '비정기')], default=0),
        ),
    ]
