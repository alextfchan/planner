from typing import Any
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from apptodolist.models import ToDoList, ToDoListItem


class ListOfToDos(ListView):
    model = ToDoList
    template_name = 'todo_index.html'


class ListOfToDoItems(ListView):
    model = ToDoListItem
    template_name = 'todo_items.html'

    def get_queryset(self):
        ''' 
        The self.kwargs['listid'] will be referenced within the urls.py file
        - The parameter will be the specific list (listid), as we do not want every
        single item created without a list filter.
        '''
        return ToDoListItem.objects.filter(list_name_id=self.kwargs['listid'])

    def get_context_data(self) -> dict[str, Any]:
        '''
        Function allows for adding to specific lists, rather than overwriting it.
        '''
        context = super().get_context_data()
        # list_name refers to the foreign key within ToDoListItem data model.
        context['list_name'] = ToDoList.objects.get(id=self.kwargs['listid'])
        return context


#CRUD Code below.
class CreateList(CreateView):
    model = ToDoList
    template_name = 'todo_list_add.html'
    fields = ['list_name']

    def get_context_data(self) -> dict[str, Any]:
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
    template_name = 'todo_items_form.html'
    fields = [
        'list_name',
        'item_name',
        'item_content',
        'status',
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

    def get_context_data(self) -> dict[str, Any]:
        '''
        https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#adding-extra-context
        '''
        context = super().get_context_data()
        list_name = ToDoList.objects.get(id=self.kwargs['listid'])
        context['list_name'] = list_name
        context['item_name'] = 'Create new item'
        return context

    def get_success_url(self):
        return reverse('app_todo:list', args=[self.object.list_name_id])


class UpdateItem(UpdateView):
    model = ToDoListItem
    template_name = 'todo_items_form.html'
    fields = [
        'list_name',
        'item_name',
        'item_content',
        'status',
    ]

    def get_context_data(self) -> dict[str, Any]:
        context = super().get_context_data()
        context['list_name'] = self.object.list_name
        context['item_name'] = 'Update item contents'
        return context

    def get_success_url(self):
        return reverse('app_todo:list', args=[self.object.list_name_id])


class DeleteList(DeleteView):
    model = ToDoList
    template_name = 'todo_list_delete.html'
    success_url = reverse_lazy('app_todo:app_todo')
    # Later potential feature:
    # can change the 'cancel' button to redirect to the list of items page, rather than index.


class DeleteItem(DeleteView):
    model = ToDoListItem
    template_name = 'todo_items_delete.html'

    def get_success_url(self):
        return reverse_lazy('app_todo:list', args=[self.kwargs['listid']])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_name'] = self.object.list_name
        return context
    