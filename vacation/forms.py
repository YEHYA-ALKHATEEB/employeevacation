from django.forms import ModelForm
from .models import Vacation

class VacationForm(ModelForm):
    class Meta:
        model = Vacation
        fields = ['description', 'datetime_from', 'datetime_to']