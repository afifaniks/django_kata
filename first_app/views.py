from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    my_dict = {
        'insert_me': "Hello There from First PY"
    }

    return render(req, 'first_app/index.html', context=my_dict)
