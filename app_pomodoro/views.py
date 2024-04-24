# from django.shortcuts import render
# from app_pomodoro.models import Timer
# from .forms import PomodoroForm
#
# def pomodoro(request):
#     timer = Timer.objects.all().order_by('name')
#     form = PomodoroForm()
#
#     if len(timer) == 0:
#         return render(request, 'pomodoro.html', {
#             'form': form,
#             'editable': False,
#             'timer': None,
#         })
#
#     return render(request, 'pomodoro.html', {
#         'form': form,
#         'editable': False,
#         'timer': timer,
#     })

from django.shortcuts import render
from .models import Timer
from .forms import TimerForm

def timer_view(request):
    timer = Timer.objects.first()
    if timer is not None:
        form = TimerForm(instance=timer)
    else:
        form = TimerForm()
    return render(request, 'pomodoro.html', {'form': form})
