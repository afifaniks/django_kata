from django.shortcuts import render
from . import form

# Create your views here.
def index(request):
    print("Request Method: " + request.method)
    new_form = form.FormName()

    if request.method == 'POST':
        new_form = form.FormName(request.POST)

        if new_form.is_valid():
            print("Validation Successful")
            print("Name: " + new_form.cleaned_data['name'])
            print("Email: " + new_form.cleaned_data['email'])
    return render(request, 'basic_form/index.html', context = {'form': new_form})