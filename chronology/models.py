# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


DAYS_OF_WEEK = (
    (0, '월'),
    (1, '화'),
    (2, '수'),
    (3, '목'),
    (4, '금'),
    (5, '토'),
    (6, '일'),
)

DATE_INTERVAL = (
    (0, '주간'),
    (1, '격주간'),
    (2, '월간'),
    (3, '1회성'),
    (4, '일간'),
    (5, '비정기'),
)

LEVEL = (
    (1, '★'),
    (2, '★★'),
    (3, '★★★'),
    (4, '★★★★'),
    (5, '★★★★★'),
)

COMMUNITY_TYPE = (
    (0, '내부'),
    (1, '외부'),
)

STUDY_STATUS = (
    (0, '진행중'),
    (1, '방학중'),
    (2, '종료'),
    (3, '이름변경(연계)'),
)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Community(models.Model):
    id = models.AutoField(primary_key=True)
    c_name_kor = models.CharField(unique=True, max_length=45)
    c_name_eng = models.CharField(unique=True, max_length=45, null=True)
    c_type = models.IntegerField(choices=COMMUNITY_TYPE, default=0)
    c_start = models.DateField()
    c_end = models.DateField(blank=True, null=True)
    c_in_charge = models.ForeignKey('Manager', db_column='c_in_charge', on_delete=models.CASCADE, blank=True, null=True)
    desc_kor = models.TextField()
    desc_eng = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    su_id = models.ForeignKey('Supporter', db_column='su_id', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'community'

    def __str__(self):
        return self.c_name_kor


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Manager(models.Model):
    id = models.AutoField(primary_key=True)
    m_name_kor = models.CharField(max_length=45)
    m_name_eng = models.CharField(max_length=45, blank=True, null=True)
    affiliation_kor = models.CharField(max_length=100)
    affiliation_eng = models.CharField(max_length=100, blank=True, null=True)
    desc_kor = models.TextField()
    desc_eng = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'manager'

    def __str__(self):
        return self.m_name_kor


class Operation(models.Model):
    id = models.AutoField(primary_key=True)
    p_id = models.ForeignKey('Part', db_column='p_id', on_delete=models.CASCADE)
    c_id = models.ForeignKey('Community', db_column='c_id', on_delete=models.CASCADE)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'operation'


class Part(models.Model):
    id = models.AutoField(primary_key=True)
    s_id = models.ForeignKey('Study', db_column='s_id', on_delete=models.CASCADE)
    part_num = models.CharField(db_column='part_num', max_length=45, default="1", blank=True, null=True)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    interval = models.IntegerField(choices=DATE_INTERVAL, default=0)
    day = models.IntegerField(choices=DAYS_OF_WEEK, default=None)
    p_in_charge = models.ForeignKey('Manager', db_column='p_in_charge', related_name='p_in_charge',
                                    on_delete=models.CASCADE, blank=True, null=True)
    p_in_charge_sub = models.ForeignKey('Manager', db_column='p_in_charge_sub', related_name='p_in_charge_sub',
                                        on_delete=models.CASCADE, blank=True, null=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=45)
    prerequisite = models.TextField(default=None)
    textbook = models.TextField(default=None)
    part_level = models.IntegerField(choices=LEVEL, default=None)

    class Meta:
        managed = True
        db_table = 'part'

    def __str__(self):
        if self.part_num != "":
            return '{} ({})'.format(self.s_id, self.part_num)
        else:
            return '{}'.format(self.s_id)


class Study(models.Model):
    id = models.AutoField(primary_key=True)
    s_name_kor = models.CharField(unique=True, max_length=45)
    s_name_eng = models.CharField(max_length=45, blank=True, null=True)
    desc_kor = models.TextField()
    desc_eng = models.TextField(blank=True, null=True)
    study_level = models.IntegerField(choices=LEVEL, default=0)
    status = models.IntegerField(choices=STUDY_STATUS, default=0)
    memo = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'study'

    def __str__(self):
        return self.s_name_kor


class Supporter(models.Model):
    su_name = models.CharField(unique=True, max_length=45)
    desc_kor = models.TextField()
    desc_eng = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'supporter'

    def __str__(self):
        return self.su_name
