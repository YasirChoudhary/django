from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .models import User, Task
from .forms import TaskForm
from django.views.generic.edit import UpdateView


'''
def index(request):
    tasks_list = Task.objects.all()
    if tasks_list:  
        context = { 'tasks_list': tasks_list }
        return render(request, 'todo/index.html', context)
    else:
        tasks_empty_list = Task()
        context = {'tasks_empty_list': tasks_empty_list}
        return render(request, 'todo/index.html', context)

'''

user_id = 0

def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
        except User.DoesNotExist:
            return HttpResponse("Username is invalid")
        else:
            if user.password == request.POST['password']:
                try:
                    #tasks_list = Task.objects.get(user=user)
                    #print(tasks_list)
                    tasks_list = user.task_set.all()
                    global user_id
                    user_id = user.id

                except Task.DoesNotExist:
                    #return HttpResponse("Task doesn't exist ")
                    pass
                    '''
                    task_list = Task()
                    user_id = user.id
                    username = user.username
                    context = {'task_list': task_list,
                                'user_id' : user_id,
                               'username' : username
                               }
                    return render(request, 'todo/index.html', context)
                    
                    
                    '''

                else:
                    context = {'tasks_list': tasks_list,
                               'username': user.username,
                               }
                    return render(request, 'todo/index.html', context)

            else:
                return HttpResponse("Your Password is in correct ")



    else:
        return render(request, 'todo/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User(username=username, password=password)
        user.save()

        return render(request, 'todo/redirect.html')

    else:
        return render(request, 'todo/signup.html')


def addtask(request):
    if request.method=='POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            #logged_user = request.user
            #user_id = logged_user.id

            global user_id

            task_text = request.POST.get('task_text')
            due_date = request.POST.get('due_date')

            task = Task(user_id=user_id ,task_text = task_text, due_date = due_date )
            task.save()

            #context = {}
            user = User.objects.get(id=user_id)
            tasks_list= user.task_set.all()

            context = {
                'tasks_list' : tasks_list,
                'username' : user.username,
            }


            #return HttpResponseRedirect(reverse(request,'todo:index'))
            return render(request, 'todo/index.html', context)

    else:
        form = TaskForm()

    return render(request, 'todo/addNewTask.html' ,{ 'form':form})


def delete(request, id):
    #text_id = id
    Task.objects.filter(id=id).delete()
    global user_id
    user = User.objects.get(id=user_id)
    tasks_list = user.task_set.all()
    context = {
        'tasks_list':tasks_list,
        'username': user.username,
    }
    #return HttpResponse("text_id ={} ".format(id))
    return render(request, 'todo/index.html', context)





def edit(request, id):
    if request.method == 'POST':
        task_text = request.POST.get('task_text')
        due_date = request.POST.get('due_date')

        task = Task.objects.get(id=id)
        #task = Task(id=id, task_text=task_text, due_date=due_date)
        task.task_text = task_text
        task.due_date = due_date
        task.save()
      #  task.save(task_text=task_text, due_date=due_date)
        #task._do_update(task_text=task_text, due_date=due_date)
        #Task.objects.select_related().filter(user_id=task)

        global user_id
        user = User.objects.get(id=user_id)
        tasks_list = user.task_set.all()

        context = {
            'tasks_list': tasks_list,
            'username': user.username,
        }

        # return HttpResponseRedirect(reverse(request,'todo:index'))
        return render(request, 'todo/index.html', context)


    else:
        context ={'id':id}
        return render(request,'todo/editTask.html', context)



    return render(request, 'polls/editTask.html', {'id':id})


def start(request):
    return render(request, 'todo/start.html')

def index(request):
    return render(request, 'todo/index.html')



'''
def index(request):
    return render(request, 'todo/index.html')
    



'''

'''
def added(request):
    return render(request, 'todo/added.html')
    
    
    user_id = user.id
    context = {'user_id':user_id}
    
class TaskUpdate(UpdateView):
    model = Task
    fields = ['task_text','due_date']
    template_name_suffix = 'todo/editTask.html'


'''
