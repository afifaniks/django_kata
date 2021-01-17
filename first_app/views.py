from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord, Topic, Webpage

# Create your views here.
def index(req):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}

    return render(req, 'first_app/index.html', context=date_dict)
