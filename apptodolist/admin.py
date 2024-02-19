from django.contrib import admin
from apptodolist.models import ToDoList, ToDoListItem

admin.site.register(ToDoList)
admin.site.register(ToDoListItem)