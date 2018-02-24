# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0015_auto_20180221_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='study',
            name='memo',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='operation',
            name='memo',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='study',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, '진행중'), (1, '방학중'), (2, '종료'), (3, '이름변경(연계)')]),
        ),
    ]
