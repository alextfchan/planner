from django.urls import path
from .views import pomodoro

app_name = 'app_pomodoro'

urlpatterns = [
    path('', pomodoro, name='app_pomodoro'),
]