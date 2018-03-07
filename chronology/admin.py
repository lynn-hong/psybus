from django.contrib import admin
from .models import Community, Event, Manager, Operation, Part, Study, Supporter


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ['c_name_kor', 'c_name_eng', 'c_type', 'c_start', 'c_end', 'c_in_charge', 'desc_kor', 'su_id', 'url', 'logo']
    list_display_links = ['c_name_kor']
    ordering = ['-c_start']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'p_id', 'e_title_kor', 'e_title_eng', 'start_time', 'end_time', 'location', 'e_desc_kor', 'e_desc_eng']
    list_display_links = ['e_title_kor']
    ordering = ['start_time']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['m_name_kor', 'm_name_eng', 'affiliation_kor', 'affiliation_eng', 'desc_kor', 'facebook']
    list_display_links = ['m_name_kor']
    ordering = ['m_name_kor']


@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ['p_id', 'c_id', 'memo']
    list_display_links = ['p_id']


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ['part_info', 'p_in_charges', 'interval', 'day', 'start', 'end', 'start_time', 'end_time', 'location',
                    'part_level', 'prerequisite', 'textbook']
    list_display_links = ['part_info']
    ordering = ['day', 'start_time', 'interval']

    def part_info(self, obj):
        if obj.part_num != "":
            return "{} ({})".format(obj.s_id, obj.part_num)
        else:
            return obj.s_id

    def p_in_charges(self, obj):
        if obj.p_in_charge_sub is None:
            return obj.p_in_charge
        else:
            return '{}, {}'.format(obj.p_in_charge, obj.p_in_charge_sub)


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ['name', 'study_level', 'desc_kor', 'status', 'memo']
    list_display_links = ['name']
    ordering = ['status', 's_name_kor']

    def name(self, obj):
        if obj.s_name_eng == "":
            return obj.s_name_kor
        else:
            return '{} ({})'.format(obj.s_name_kor, obj.s_name_eng)


@admin.register(Supporter)
class SupporterAdmin(admin.ModelAdmin):
    list_display = ['su_name', 'desc_kor', 'logo', 'url']
    list_display_links = ['su_name']
    ordering = ['su_name']
