from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)
from apptodolist.models import ToDoList, ToDoListItem

class ListOfToDos(ListView):
    model = ToDoList
    # template_name allows you to generate a HTML dynamically.
    # Will allow for dynamic HTML links for each list ID.
    template_name = 'todoindex.html'


class ListOfToDoItems(ListView):
    model = ToDoListItem
    template_name = 'todoitems.html'

    def get_queryset(self):
        ''' 
        The self.kwargs["listid"] will be referenced within the urls.py file
        - The parameter will be the specific list (listid), as we do not want every
        single item created without a list filter.
        '''
        return ToDoListItem.objects.filter(list_name_id=self.kwargs["listid"])
    
    def get_context_data(self) -> dict[str, Any]:
        context = super().get_context_data()
        # list_name refers to the foreign key within ToDoListItem data model.
        context["list_name"] = ToDoList.objects.get(id=self.kwargs["listid"])
        return context
    

# onclick="location.href='{% url "app_todo:list" todolist.id %}'">
