from django.forms import ModelForm
from .models import Tire

class TireForm(ModelForm):
    class Meta:
        model = Tire
        fields = ['date', 'size']