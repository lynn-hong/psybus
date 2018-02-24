# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0012_auto_20180221_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='part_level',
            field=models.IntegerField(default=None, choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')]),
        ),
        migrations.AlterField(
            model_name='study',
            name='study_level',
            field=models.IntegerField(default=0, choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')]),
        ),
    ]
