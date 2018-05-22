from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import User


def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
        except User.DoesNotExist:
            return HttpResponse("This username doen't exist")
        else:
            if user.password == request.POST['password']:
                request.session['id_user'] = user.id
                return render(request, 'user/home.html', {'user': user})

            else:
                return HttpResponse("your username and password didn't match")
    else:

        return render(request, 'user/login.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = User(username=username, password=password)
        user.save()

        return render(request, 'user/redirect.html')
    else:
        return render(request, 'user/signup.html')


    '''
    IMP Links
    https://docs.djangoproject.com/en/2.0/topics/http/sessions/
    
    
    '''







