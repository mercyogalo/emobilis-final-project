from django.contrib import admin
from .models import Farmer, Task, Worker,SupervisorCreateworker, SupervisorCreatetask,Contact

# Register your models here.
admin.site.register(Farmer)
admin.site.register(Task)
admin.site.register(Worker)
admin.site.register(SupervisorCreateworker)
admin.site.register(SupervisorCreatetask)
admin.site.register(Contact)