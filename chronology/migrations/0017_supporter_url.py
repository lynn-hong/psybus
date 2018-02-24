# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0016_auto_20180221_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='supporter',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
