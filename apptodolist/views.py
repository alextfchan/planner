from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from apptodolist.models import ToDoList, ToDoListItem

class ListOfToDos(ListView):
    model = ToDoList
    # template_name allows you to generate a HTML dynamically.
    # Will allow for dynamic HTML links for each list ID.
    template_name = 'todo_index.html'


class ListOfToDoItems(ListView):
    model = ToDoListItem
    template_name = 'todo_items.html'

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


#CRUD Code below.

class CreateList(CreateView):
    model = ToDoList
    template_name = 'todo_list_add.html'
    fields = ['list_name']

    def get_context_data(self):
        '''
        https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#adding-extra-context
        '''
        context = super().get_context_data()
        context['list_name'] = 'Add a new list'
        return context

    def get_success_url(self):
        return reverse('app_todo:app_todo')


class CreateItem(CreateView):
    model = ToDoListItem
    template_name = 'todo_items_add.html'
    fields = [
        'list_name',
        'item_name',
        'item_content',
    ]

    def get_initial(self):
        '''
        Returns a dictionary containing initial data for the form.
        - listid is from the ToDoList class (in Models), list_id_url method.
        - list_name ToDoList class property.

        '''
        initial_data = super().get_initial()
        list_name = ToDoList.objects.get(id=self.kwargs['listid'])
        initial_data['list_name'] = list_name
        return initial_data

    def get_context_data(self):
        '''
        https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#adding-extra-context
        '''
        context = super().get_context_data()
        list_name = ToDoList.objects.get(id=self.kwargs['listid'])
        context['list_name'] = list_name
        context['item_name'] = 'Create a new item'
        return context

    def get_success_url(self):
        return reverse('app_todo:list', args=[self.object.list_name_id])
