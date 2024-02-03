from django.contrib import admin
from apptodolist.models import ToDoList, ToDoListItem
# Register your models here.

admin.site.register(ToDoList)
admin.site.register(ToDoListItem)