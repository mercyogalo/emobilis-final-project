from django.urls import path
from . import views

app_name="farmers"

urlpatterns = [
  path("home/", views.index, name="home"),
  path("tasksPage/", views.tasksPage, name="tasksPage"),
  path("workersPage/", views.workersPage, name="workersPage"),
  path("createWorkersPage/", views.createWorkersPage, name="createWorkersPage"),
  path("createTasksPage/", views.createTasksPage, name="createTasksPage"),
  path("editTask/<id>",views.editTask, name='editTask'),
  path("deleteTask/<id>",views.deleteTask, name='deleteTask'),
  path("editWorker/<id>",views.editWorker, name='editWorker'),
  path("deleteWorker/<id>",views.deleteWorker, name='deleteWorker'),
  path("contact/",views.contact, name="contact"),
  path("workerHome/",views.workerHome, name="workerHome"),
  path("workerTask/",views.workerTask, name="workerTask"),
  path("supervisorHome/", views.supervisorHome, name="supervisorHome"),
  path("supervisorCreateTaskPage/",views.supervisorCreateTaskPage,name="supervisorCreateTaskPage"),
  path("supervisorTaskPage/",views.supervisorTaskPage,name="supervisorTaskPage"),
  path("supervisorEditTaskPage/<id>",views.supervisorEditTaskPage,name="supervisorEditTaskPage"),
    path("supervisorTaskDelete/<id>",views.supervisorTaskDelete, name="supervisorTaskDelete"),
    path("supervisorEditWorkerPage/<id>",views.supervisorEditWorkerPage,name="supervisorEditWorkerPage"),
    path("supervisorWorkerDelete/<id>",views.supervisorWorkerDelete,name="supervisorWorkerDelete"),
  path("supervisorWorkerPage/",views.supervisorWorkerPage, name="supervisorWorkerPage"),
  path("supervisorCreateWorkerPage/",views.supervisorCreateWorkerPage, name="supervisorCreateWorkerPage"),
  path("SupervisorProfilePage/", views.SupervisorProfilePage, name="SupervisorProfilePage"),
   path("MainProfilePage/", views.MainProfilePage, name="MainProfilePage"),
    path("WorkerProfilePage/", views.WorkerProfilePage, name="WorkerProfilePage"),
]