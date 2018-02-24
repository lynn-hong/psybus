# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chronology', '0017_supporter_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
