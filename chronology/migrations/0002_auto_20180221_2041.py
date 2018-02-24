# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={},
        ),
        migrations.AddField(
            model_name='community',
            name='c_type',
            field=models.CharField(default=0, max_length=1, choices=[(0, '내부'), (1, '외부')]),
        ),
    ]
