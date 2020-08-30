from django.shortcuts import render

from polls.models import AccessRecord


# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by("date")
    data_dict = {'access_records': webpages_list}
    return render(request, 'index.html', context=data_dict)
