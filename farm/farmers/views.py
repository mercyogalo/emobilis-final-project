from django.shortcuts import render,redirect,get_object_or_404
from . models import Farmer, Task, Worker, SupervisorCreatetask, SupervisorCreateworker, Contact
from django.views.decorators.csrf import csrf_exempt
from authentication.models import CustomUser

#Admins Pages
# Create your views here.


@csrf_exempt
def index(request):
    tasks=Task.objects.all()
    workers=Worker.objects.all()
    supervisorworkers=SupervisorCreateworker.objects.all()
    supervisortasks=SupervisorCreatetask.objects.all()
    mainProfiles=get_object_or_404(CustomUser,  id=request.user.id)
    context={
        'tasks': tasks,
        'workers':workers,
        'supervisorworkers': supervisorworkers,
        'supervisortasks': supervisortasks,
        'mainProfiles': mainProfiles
    }
    return render(request,'main/index.html',context)


def workersPage(request):
    workers=Worker.objects.all()
    supervisorworkers=SupervisorCreateworker.objects.all()
    context={
        'workers':workers,
        'supervisorworkers':supervisorworkers
    }
    return render(request,'main/workers-page.html',context)


def createWorkersPage(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        role=request.POST['role']
        email=request.POST['email']
        worktype=request.POST['worktype']
        status=request.POST['status'].lower()
        image=request.FILES['image']
        
        worker=Worker(name=name, phone=phone, role=role, email=email, worktype=worktype,status=status,image=image)
        create_user  = CustomUser.objects.create_user(username=name, name=name,  email=email, user_type=role.lower(), password=email)
        create_user.save()
        worker.save()
        
        return redirect('farmers:workersPage')
    
    return render(request,'main/create-workers.html')

def editWorker(request, id):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        role=request.POST['role']
        email=request.POST['email']
        worktype=request.POST['worktype']
        status=request.POST['status'].lower()
        image=request.FILES['image']
        
        
        workers=Worker.objects.get(id=id)
        
        workers.name = name
        workers.phone = phone
        workers.role = role
        workers.email = email
        workers.worktype = worktype
        workers.status = status
        workers.image = image
        
        workers.save()
        return redirect('farmers:workersPage')
    # just edit these 
    workers=Worker.objects.get(id=id)
    return render(request, 'main/edit-worker.html',{'workers': workers})

def deleteWorker(request, id):
    workers=Worker.objects.get(id=id)
    user = CustomUser.objects.get(name=workers.name).delete()
    workers.delete()
    return redirect('farmers:workersPage')

def createTasksPage(request):
    if request.method=="POST":
        name=request.POST['name']
        role=request.POST['role']
        heading=request.POST['heading']
        description=request.POST['description']
        days=request.POST['days']
        
        task=Task(name=name,role=role,heading=heading,description=description,days=days)
        task.save()
        return redirect('farmers:tasksPage')    
               
    return render(request,'main/create-tasks.html')




def tasksPage(request):
    tasks=Task.objects.all()
    return render(request,'main/tasks-page.html',{'tasks': tasks})

def editTask(request, id):
    if request.method=="POST":
        name = request.POST['name']
        role = request.POST['role']
        heading = request.POST['heading']
        description = request.POST['description']
        days = request.POST['days']

        tasks=Task.objects.get(id = id)

        tasks.name = name
        tasks.role = role
        tasks.heading = heading
        tasks.description = description
        tasks.days = days

        tasks.save()
        return redirect('farmers:tasksPage')
        
    tasks=Task.objects.get(id = id)
    return render(request, 'main/edit-task.html',{'tasks': tasks})

def deleteTask(request, id):
    tasks=Task.objects.get(id=id)
    tasks.delete()
    
    return redirect('farmers:tasksPage')

    


    
    
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        image=request.FILES['image']
        
        contact=Contact(name=name, email=email, subject=subject, message=message, image=image)
        contact.save()
        return redirect('/workerHome/')
    return render(request,'workers/contact.html')



#Workers pages
def workerHome(request):
    profiles=get_object_or_404(SupervisorCreateworker,email=request.user.email)
    supervisortasks=SupervisorCreatetask.objects.all()
    context={
        'supervisortasks': supervisortasks,
        'profiles':profiles
    }
    return render(request,'workers/worker-home.html',context)


def workerTask(request):
    if request.user.is_authenticated:
        supervisortasks = SupervisorCreatetask.objects.all()
        context = {
            'supervisortasks': supervisortasks,
        }
        return render(request, 'workers/worker-task.html', context)
    else:
        return redirect('login')



def supervisorHome(request):
        supervisortasks = SupervisorCreatetask.objects.all()
        supervisorworkers = SupervisorCreateworker.objects.all()
        supervisorProfiles=get_object_or_404(Worker,email=request.user.email)

        context = {
            'supervisortasks': supervisortasks,
            'supervisorworkers': supervisorworkers,
            'supervisorProfiles':supervisorProfiles
            
        }
        return render(request, 'supervisor/home.html', context)



def supervisorCreateTaskPage(request):
    if request.method=="POST":
        name=request.POST['name']
        role=request.POST['role']
        heading=request.POST['heading']
        description=request.POST['description']
        days=request.POST['days']
      
        
        supervisortask=SupervisorCreatetask(name=name,role=role,heading=heading,description=description,days=days)
        supervisortask.save()
        return redirect('/supervisorTaskPage/')    
    
    return render(request,'supervisor/create-task.html')


def supervisorEditTaskPage(request,id):
    if request.method=="POST":
        name = request.POST['name']
        role = request.POST['role']
        heading = request.POST['heading']
        description = request.POST['description']
        days = request.POST['days']

        supervisortasks=SupervisorCreatetask.objects.get(id = id)

        supervisortasks.name = name
        supervisortasks.role = role
        supervisortasks.heading = heading
        supervisortasks.description = description
        supervisortasks.days = days

        supervisortasks.save()
        return redirect('/supervisorTaskPage/')
        
    supervisortasks=SupervisorCreatetask.objects.get(id = id)
    return render(request,'supervisor/edit-task.html',{'supervisortasks': supervisortasks})

def supervisorTaskDelete(request,id):
    supervisortasks=SupervisorCreatetask.objects.get(id = id)
    supervisortasks.delete()
    return redirect('/supervisorTaskPage/')

def supervisorTaskPage(request):
    supervisortasks=SupervisorCreatetask.objects.all()
    context={
        'supervisortasks': supervisortasks
    }
    return render(request, 'supervisor/task-page.html',context)



def supervisorCreateWorkerPage(request):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        role=request.POST['role']
        email=request.POST['email']
        worktype=request.POST['worktype']
        status=request.POST['status'].lower()
        image=request.FILES['image']
        
        supervisorworker=SupervisorCreateworker(name=name, phone=phone, role=role, email=email, worktype=worktype,status=status,image=image)
        create_user  = CustomUser.objects.create_user(username=name, email=email, user_type=role.lower(), password=email)
        create_user.save()
        supervisorworker.save()
        
        return redirect('/supervisorWorkerPage/')
    return render(request, 'supervisor/create-worker.html')



def supervisorEditWorkerPage(request, id):
    if request.method=="POST":
        name=request.POST['name']
        phone=request.POST['phone']
        role=request.POST['role']
        email=request.POST['email']
        worktype=request.POST['worktype']
        status=request.POST['status'].lower()
        image=request.FILES['image']
        
        
        supervisorworkers=SupervisorCreateworker.objects.get(id=id)
        
        supervisorworkers.name = name
        supervisorworkers.phone = phone
        supervisorworkers.role = role
        supervisorworkers.email = email
        supervisorworkers.worktype = worktype
        supervisorworkers.status = status
        supervisorworkers.image = image
        
        supervisorworkers.save()
        return redirect('/supervisorWorkerPage/')
    
    supervisorworkers=SupervisorCreateworker.objects.get(id=id)
    return render(request, 'supervisor/edit-worker.html',{'supervisorworkers': supervisorworkers})

def supervisorWorkerDelete(request, id):
    supervisorworkers=SupervisorCreateworker.objects.get(id=id)
    supervisorworkers.delete()
    return redirect('/workersPage/')


def supervisorWorkerPage(request):
    supervisorworkers=SupervisorCreateworker.objects.all()
    context={
        'supervisorworkers': supervisorworkers,
    }
    return render(request,'supervisor/worker.html',context)




def MainProfilePage(request):
    mainProfiles=get_object_or_404(CustomUser, id=request.user.id)
    context={
        'mainProfiles': mainProfiles
    }
    return render(request,'main/profile.html',context)



def SupervisorProfilePage(request):
    supervisorProfiles=get_object_or_404(Worker,email=request.user.email)
    context={
        'supervisorProfiles':supervisorProfiles
    }
    return render(request,'supervisor/profile.html',context)




def WorkerProfilePage(request):
    profiles=get_object_or_404(SupervisorCreateworker,email=request.user.email)
    context={
        'profiles': profiles
    }
    return render(request,'workers/profile.html',context)


