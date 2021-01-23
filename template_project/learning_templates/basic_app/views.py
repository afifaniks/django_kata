from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': "Afif",
        "number": 7979
    }
    return render(request, 'basic_app/index.html', context)
    
def relative(request):
    return render(request, 'basic_app/relative_url_templates.html')

def other(request):
    return render(request, 'basic_app/other.html')