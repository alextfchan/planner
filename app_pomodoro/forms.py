from django import forms
from .models import Timer

class PomodoroForm(forms.ModelForm):
    class Meta:
        model = Timer
        fields = ['name', 'hours', 'minutes', 'seconds']
        widgets = {
            'name': forms.TextInput(attrs={'required': 'required'}),
            'hours': forms.NumberInput(attrs={'required': 'required'}),
            'minutes': forms.NumberInput(attrs={'required': 'required'}),
            'seconds': forms.NumberInput(attrs={'required': 'required'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        hours = cleaned_data.get('hours', 0)
        minutes = cleaned_data.get('minutes', 0)
        seconds = cleaned_data.get('seconds', 0)

        if hours < 0 or hours > 24:
            raise forms.ValidationError('Hours must be between 0 and 24')
        if minutes < 0 or minutes > 59:
            raise forms.ValidationError('Minutes must be between 0 and 59')
        if seconds < 0 or seconds > 59:
            raise forms.ValidationError('Seconds must be between 0 and 59')
        return cleaned_data