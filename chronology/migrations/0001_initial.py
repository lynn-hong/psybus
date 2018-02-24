# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(null=True, blank=True, max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(null=True, blank=True, max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(primary_key=True, serialize=False, max_length=40)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('c_name_kor', models.CharField(unique=True, max_length=45)),
                ('c_name_eng', models.CharField(null=True, unique=True, max_length=45)),
                ('c_start', models.DateField()),
                ('c_end', models.DateField(null=True, blank=True)),
                ('desc_kor', models.TextField()),
                ('desc_eng', models.TextField(null=True, blank=True)),
                ('url', models.TextField(null=True, blank=True)),
                ('logo', models.CharField(null=True, blank=True, max_length=100)),
            ],
            options={
                'db_table': 'community',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('m_name_kor', models.CharField(max_length=45)),
                ('m_name_eng', models.CharField(null=True, blank=True, max_length=45)),
                ('affiliation_kor', models.CharField(max_length=100)),
                ('affiliation_eng', models.CharField(null=True, blank=True, max_length=100)),
                ('desc_kor', models.TextField()),
                ('desc_eng', models.TextField(null=True, blank=True)),
                ('facebook', models.CharField(null=True, blank=True, max_length=255)),
            ],
            options={
                'db_table': 'manager',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('memo', models.TextField(default=None)),
                ('c_id', models.ForeignKey(db_column='c_id', to='chronology.Community')),
            ],
            options={
                'db_table': 'operation',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('part', models.CharField(max_length=45)),
                ('start', models.DateField()),
                ('end', models.DateField(null=True, blank=True)),
                ('interval', models.CharField(choices=[(0, '매주'), (1, '격주'), (2, '1회성'), (3, '매일')], default=0, max_length=1)),
                ('day', models.CharField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')], default=None, max_length=1)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(max_length=45)),
                ('prerequisite', models.TextField(default=None)),
                ('textbook', models.TextField(default=None)),
                ('part_level', models.CharField(choices=[(0, '★'), (1, '★★'), (2, '★★★'), (3, '★★★★'), (4, '★★★★★')], default=None, max_length=1)),
            ],
            options={
                'db_table': 'part',
            },
        ),
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('s_name_kor', models.CharField(unique=True, max_length=45)),
                ('s_name_eng', models.CharField(null=True, blank=True, max_length=45)),
                ('s_in_charge', models.CharField(null=True, blank=True, max_length=45)),
                ('desc_kor', models.TextField()),
                ('desc_eng', models.TextField(null=True, blank=True)),
                ('study_level', models.CharField(choices=[(0, '★'), (1, '★★'), (2, '★★★'), (3, '★★★★'), (4, '★★★★★')], default=0, max_length=1)),
                ('status', models.CharField(choices=[(0, '진행중'), (1, '방학중')], default=0, max_length=1)),
            ],
            options={
                'db_table': 'study',
            },
        ),
        migrations.CreateModel(
            name='Supporter',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('su_name', models.CharField(unique=True, max_length=45)),
                ('desc_kor', models.TextField()),
                ('desc_eng', models.TextField(null=True, blank=True)),
                ('logo', models.CharField(null=True, blank=True, max_length=100)),
            ],
            options={
                'db_table': 'supporter',
            },
        ),
        migrations.AddField(
            model_name='part',
            name='s_id',
            field=models.ForeignKey(db_column='s_id', to='chronology.Study'),
        ),
        migrations.AddField(
            model_name='operation',
            name='p_id',
            field=models.ForeignKey(db_column='p_id', to='chronology.Part'),
        ),
        migrations.AddField(
            model_name='community',
            name='c_in_charge',
            field=models.ForeignKey(to='chronology.Manager', null=True, db_column='c_in_charge', blank=True),
        ),
        migrations.AddField(
            model_name='community',
            name='su_id',
            field=models.ForeignKey(to='chronology.Supporter', null=True, db_column='su_id', blank=True),
        ),
    ]
