from django.forms import ModelForm
from .models import Personne

class PersonneForm(ModelForm):
    class Meta:
        model = Personne
        fields = ['name', 'subname', 'birth', 'email', 'tel', 'role']