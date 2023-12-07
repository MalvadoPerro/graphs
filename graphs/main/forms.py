from .models import Count
from django.forms import ModelForm, NumberInput

class CountForm(ModelForm):
    class Meta:
        model = Count
        fields = ['count']

        widgets = {
            'count': NumberInput(attrs={
                'type': 'range',
                'min': '1',
                'max': '20',
                'value': '5',
                'step': '1',
                'list': 'tickmarks'
            })
        }
