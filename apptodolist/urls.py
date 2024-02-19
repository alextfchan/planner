from django.urls import include, path
from . import views

# app_name is required here since we are using a project wide template. Not one that is within this app.
app_name = 'app_todo'


# name = parameter that will match with the HTML macro.
urlpatterns = [
    # url: /planner/ name: 'app_todo' will match with HTML macro.
    path('', views.ListOfToDos.as_view(), name = 'app_todo'),

    # url: /planner/<id> name: 'listid' will match with HTML macro.
    # <int:list_id> is referring to the parameter created in views. (get_lists_query function)
    path('<int:listid>/',
         views.ListOfToDoItems.as_view(),
         name = 'list'),


    # Create List and Item patterns
    path('add/',
         views.CreateList.as_view(),
         name='list_add'),

    path('<int:listid>/item/add/',
         views.CreateItem.as_view(),
         name='item_add'),

    # Update Item pattern
    path('<int:listid>/item/<int:pk>/',
         views.UpdateItem.as_view(),
         name='item_update'),

    # Delete List and Item patterns
    path('<int:pk>/delete/',
         views.DeleteList.as_view(),
         name='list_delete'),

    path('<int:listid>/item/<int:pk>/delete/',
         views.DeleteItem.as_view(),
         name='item_delete'),
]