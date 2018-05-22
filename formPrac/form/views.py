from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_Name(request):

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')

    else:
        form = NameForm()

    return render(request, 'form/name.html', {'form': form})


