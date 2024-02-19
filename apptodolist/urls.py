from django.urls import path
from . import views

# app_name is required here since we are using a project wide template (header.html).
# name = parameter that will match with the HTML macro.
app_name = 'app_todo'


urlpatterns = [
    # Starting url: /planner/
    path('',
         views.ListOfToDos.as_view(),
         name = 'app_todo'),

    # Patterns for lists
    path('<int:listid>/',
         views.ListOfToDoItems.as_view(),
         name = 'list'),
    path('add/',
         views.CreateList.as_view(),
         name='list_add'),
    path('<int:pk>/delete/',
         views.DeleteList.as_view(),
         name='list_delete'),

    # Patterns for items 
    path('<int:listid>/item/add/',
         views.CreateItem.as_view(),
         name='item_add'),
    path('<int:listid>/item/<int:pk>/',
         views.UpdateItem.as_view(),
         name='item_update'),
    path('<int:listid>/item/<int:pk>/delete/',
         views.DeleteItem.as_view(),
         name='item_delete'),
]
