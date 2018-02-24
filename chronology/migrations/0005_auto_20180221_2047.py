# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0004_auto_20180221_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='status',
            field=models.IntegerField(choices=[(0, '진행중'), (1, '방학중')], default=0),
        ),
        migrations.AlterField(
            model_name='study',
            name='study_level',
            field=models.IntegerField(choices=[(0, '★'), (1, '★★'), (2, '★★★'), (3, '★★★★'), (4, '★★★★★')], default=0),
        ),
    ]
