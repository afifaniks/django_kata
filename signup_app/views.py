from django.shortcuts import render
from signup_app.forms import NewUserForm

# Create your views here.
def index(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request, 'signup_app/users.html', context={'form': form})
