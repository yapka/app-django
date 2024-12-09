from django.shortcuts import render
from django.http import HttpResponse

from test_app.models import Personne
from impot_app.models import Impot

# Create your views here.
def home(request):
    impot=Impot.objects.all()
    person=Personne.objects.all()
    
    content={
        'impot':impot,
        'persons':person
    }
    return render(request, 'base.html', content)