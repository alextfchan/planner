from django.urls import path
# from .views import pomodoro
from .views import timer_view

app_name = 'app_pomodoro'

urlpatterns = [
    # path('', pomodoro, name='app_pomodoro'),
    path('', timer_view, name='app_pomodoro'),
]