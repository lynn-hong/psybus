from django.views.generic import TemplateView
from .models import Community, Manager, Operation, Part, Study, Supporter, COMMUNITY_TYPE, DAYS_OF_WEEK, DATE_INTERVAL, LEVEL
from django.template.defaulttags import register
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.db.models import Q

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def get_commu(c_type):
    groups = dict()
    rows = Community.objects.filter(c_type=c_type) \
        .extra({'s': "DATE_FORMAT(c_start, '%%b. %%Y')", 'e': "DATE_FORMAT(c_end, '%%b. %%Y')"}) \
        .values('id', 's', 'e', 'c_start', 'c_name_kor', 'c_name_eng', 'c_in_charge__m_name_kor',
                'desc_kor', 'url', 'logo', 'su_id__su_name') \
        .order_by('-c_start')
    for entry in rows:
        if entry['e'] is None:
            entry['range_ko'] = "%s - 현재" % entry['s']
            entry['range_en'] = "%s - CURRENT" % entry['s']
        else:
            entry['range_ko'] = "%s - %s (종료)" % (entry['s'], entry['e'])
            entry['range_en'] = "%s - %s (end)" % (entry['s'], entry['e'])

        entry['year'] = entry['c_start'].year
        if entry['year'] not in groups:
            groups[entry['year']] = [entry]
        else:
            groups[entry['year']].append(entry)
    return groups


def get_links(c_type):
    rows = Community.objects.filter(c_type=c_type).all()\
             .order_by('c_start')    # 0=="내부"
    for entry in rows:
        if entry.c_end is not None:
            entry.live = False
        else:
            entry.live = True
    return rows


class Index(TemplateView):
    template_name = 'chronology/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        # group names
        context['group_names'] = Community.objects.filter(c_type=0).filter(~Q(id=1)).all()    # 0=="내부"
        # group informs
        context['groups'] = sorted(get_commu(0).items(), reverse=True)    # 0=="내부"
        # supporters
        context['supporters'] = Supporter.objects.all()
        return context


class Links(TemplateView):
    template_name = 'chronology/links.html'

    def get_context_data(self, **kwargs):
        context = super(Links, self).get_context_data(**kwargs)
        # groups
        context['in_groups'] = get_links(0)    # 0=="내부"
        context['out_groups'] = get_links(1)    # 1=="외부"
        return context


def get_study_info(pk):
    operations = Operation.objects.filter(c_id=pk).all()\
        .values('id', 'p_id', 'c_id', 'memo',
                'p_id__part_num', 'p_id__start', 'p_id__end', 'p_id__interval', 'p_id__day', 'p_id__p_in_charge', 'p_id__p_in_charge_sub',
                'p_id__start_time', 'p_id__end_time', 'p_id__location', 'p_id__prerequisite', 'p_id__textbook', 'p_id__part_level',
                'p_id__s_id', 'p_id__s_id__s_name_kor', 'p_id__s_id__s_name_eng', 'p_id__s_id__desc_kor', 'p_id__s_id__desc_eng',
                'p_id__p_in_charge__m_name_kor') \
        .order_by('-p_id__start')
    for entry in operations:
        # date range
        if entry['p_id__end'] is None:
            entry['range_ko'] = "%s - 현재" % entry['p_id__start'].strftime('%Y-%m-%d')
            entry['range_en'] = "%s - CURRENT" % entry['p_id__start'].strftime('%Y-%m-%d')
        else:
            entry['range_ko'] = "%s - %s" % (entry['p_id__start'].strftime('%Y-%m-%d'), entry['p_id__end'].strftime('%Y-%m-%d'))
            entry['range_en'] = "%s - %s" % (entry['p_id__start'].strftime('%Y-%m-%d'), entry['p_id__end'].strftime('%Y-%m-%d'))

        # study status
        if entry['p_id__start'] > date.today():
            entry['status'] = "예정"
        elif entry['p_id__end'] is None:
            entry['status'] = "진행중"
        else:
            entry['status'] = "종료"

        # day and interval
        entry['day'] = DAYS_OF_WEEK[entry['p_id__day']][1]
        entry['interval'] = DATE_INTERVAL[entry['p_id__interval']][1]
        entry['level'] = LEVEL[entry['p_id__part_level']-1][1]

    return operations

def group_detail(request, pk):
    group_detail = get_object_or_404(Community, pk=pk)
    studies = get_study_info(pk)

    return render(request, 'chronology/group_detail.html',
                    {'group_detail': group_detail,
                     'studies': studies,
                    }
                  )

