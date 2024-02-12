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

    def list_id_url(self):
        ''' Returns the URL for the specific ToDoList. '''
        return reverse ('listid', args=[self.id])

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

    def item_id_url(self):
        ''' Returns the URL for the specific ToDoListItem. '''
        return reverse('itemid', args=[str(self.list_name.id), str(self.id)])
    
    def __str__(self):
        return f"{self.item_name}, from list: {self.list_name}"




    pass

# CRUD


# Lines 13 to 14 and 26 to 29 implement the .get_absolute_url() method, a Django convention for data models. This function returns the URL for the particular data item. This allows you to reference the URL conveniently and robustly in your code. The return statement of both implementations of .get_absolute_url() uses reverse() to avoid hard-coding the URL and its parameters.

