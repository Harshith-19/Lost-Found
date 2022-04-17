from django.forms import ModelForm
from .models import LostItem, FoundItem

class LostForm(ModelForm):
    class Meta:
        model = LostItem
        fields = '__all__'

class FoundForm(ModelForm):
    class Meta:
        model = FoundItem
        fields = '__all__'