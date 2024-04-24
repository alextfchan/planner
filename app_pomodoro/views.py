from django.shortcuts import render
from app_pomodoro.models import Timer
from .forms import PomodoroForm

def pomodoro(request):
    timer = Timer.objects.all().order_by('name')
    form = PomodoroForm()

    if len(timer) == 0:
        return render(request, 'pomodoro.html', {
            'form': form,
            'editable': False,
            'timer': None,
        })

    return render(request, 'pomodoro.html', {
        'form': form,
        'editable': False,
        'timer': timer,
    })
