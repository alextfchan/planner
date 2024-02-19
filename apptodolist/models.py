from django.db import models
# from django.utils import timezone
from django.urls import reverse


# defining data models. these are superclasses extending to django.db.models.Model.
    # using models.Models to create superclasses giving a unique id field.
# requires 2 models:
    # 1. ToDoList (actual title),
    # 2. ToDoListItem (an individual entry in a list).

class ToDoList(models.Model):
    ''' This class is for each ToDoList title. '''

    list_name = models.CharField(max_length=100, unique = True)
    created_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        ''' Returns the URL for the specific ToDoList. '''
        return reverse ('list', args=[self.id])

    def __str__(self):
        return self.list_name

class ToDoListItem(models.Model):
    '''
    This class is for each individual item within a ToDoList.
    ---
    Status = Whether the item has been completed or not.
    '''

    list_name = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100, unique = False)
    item_content = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        ''' Returns the URL for the specific ToDoListItem. '''
        return reverse('item_update', args=[str(self.list_name.id), str(self.id)])

    def __str__(self):
        return f"{self.item_name}, from list: {self.list_name}"