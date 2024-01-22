from django.urls import path
from . import views

app_name = 'app_todo'
urlpatterns = [
    # path('', views.test),
    path('', views.todo, name = 'app_todo')
]