# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0002_auto_20180221_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='c_type',
            field=models.IntegerField(default=0, max_length=1, choices=[(0, '내부'), (1, '외부')]),
        ),
    ]
