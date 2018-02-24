# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0006_auto_20180221_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='day',
            field=models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=None),
        ),
        migrations.AlterField(
            model_name='part',
            name='interval',
            field=models.IntegerField(choices=[(0, '매주'), (1, '격주'), (2, '1회성'), (3, '매일')], default=0),
        ),
        migrations.AlterField(
            model_name='part',
            name='part_level',
            field=models.IntegerField(choices=[(0, '★'), (1, '★★'), (2, '★★★'), (3, '★★★★'), (4, '★★★★★')], default=None),
        ),
    ]
