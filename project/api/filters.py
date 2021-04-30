from django_filters import FilterSet, CharFilter ,DateFilter, Filter
from .models import Metrics
from django.db.models import Sum


def group_by_filter(self, queryset, name, value):
    params = [val.strip() for val in value.split(',')]
    return queryset.values(*params).annotate(clicks=Sum('clicks'), imperessions=Sum('impressions'),
                                             installs=Sum('installs'), revenue=Sum('revenue'), spend=Sum('spend'))

    sort_by_date = CharFilter(method='sort_by_date_filter')
    sort_by_channel = CharFilter(method='sort_by_channel_filter')
    sort_by_country = CharFilter(method='sort_by_country_filter')
    sort_by_spend = CharFilter(method='sort_by_spend_filter')
    sort_by_revenue = CharFilter(method='sort_by_revenue_filter')
    sort_by_os = CharFilter(method='sort_by_os_filter')
    sort_by_impressions = CharFilter(method='sort_by_imperessions_filter')
    sort_by_clicks = CharFilter(method='sort_by_clicks_filter')
    sort_by_installs = CharFilter(method='sort_by_installs_filter')
    
    sort_by_cpi = CharFilter(method='sort_by_cpi_filter')


class Filter_by_User(FilterSet):
    channel=CharFilter(lookup_expr='icontains')
    country=CharFilter(lookup_expr='icontains')
    os=CharFilter(lookup_expr='icontains')
    from_date=DateFilter(field_name='date',lookup_expr='gt')
    upto_date=DateFilter(field_name='date',lookup_expr='gt')
    date=DateFilter(field_name='date',lookup_expr='exact')
    
    group_by = group_by_filter



    def sort_by_date_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-date')
        else:
            return queryset.order_by('date')

    def sort_by_channel_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-channel')
        else:
            return queryset.order_by('channel')

    def sort_by_country_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-country')
        else:
            return queryset.order_by('country')

    def sort_by_os_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-os')
        else:
            return queryset.order_by('os')
        
    def sort_by_revenue_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-revenue')
        else:
            return queryset.order_by('revenue')
        
    def sort_by_impressions_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-imperessions')
        else:
            return queryset.order_by('impressions')

    def sort_by_clicks_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-clicks')
        else:
            return queryset.order_by('clicks')

    def sort_by_installs_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-installs')
        else:
            return queryset.order_by('install')

    def sort_by_spend_filter(self,queryset,name,value):
        if value == 'desc':
            return queryset.order_by('-spend')
        else:
            return queryset.order_by('spend')



    def sort_by_cpi_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-cpi')
        else:
            return queryset.order_by('cpi')


    class Meta:
        model=Metrics
        fields = ['spend','os','installs','revenue','channel','country','impressions','clicks','date', 'cpi']
