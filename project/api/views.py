import django_filters
from .models import Metrics
from .serializer import DataSerializer
from .filters import Filter_by_User
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render
#from django.http import HttpResponse
#from .forms import MetricsForm
import csv




class Pagination(PageNumberPagination):
    page_size = 50
    last_page_strings = ('last',)

class MetricsSearchView(ListAPIView):
    serializer_class = DataSerializer
    queryset = Metrics.objects.all()
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_class = Filter_by_User

    def get_queryset(self):
        queryset = self.queryset
        fields = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue','cpi']
        return queryset

"""
def upload_csv(request):
    #return HttpResponse('drop the file here')
    form = MetricsForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = MetricsForm()
        obj = Metrics.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                for i, row in enumerate(reader):
                    if i==0:
                        pass
                else:
                    print(row)



    return render(request, 'Templates/upload.html', {'form': form}) """
