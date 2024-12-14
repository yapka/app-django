from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from test_app.models import Personne
from impot_app.models import Impot

from test_app.forms import PersonneForm
# Create your views here.
def home(request):
    impot=Impot.objects.all()
    person=Personne.objects.all()
    
    content={
        'impot':impot,
        'persons':person
    }
    return render(request, 'base.html', content)


def create(request):
    form=PersonneForm()
    
    if request.method=='POST':
        
        form=PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
            'form':form}
    
    return render(request, 'register.html', context)

def update(request,pk):
    person=Personne.objects.get(id=pk)
    form=PersonneForm(instance=person)
    if request.method=='POST':
        form=PersonneForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/')
            # return render(request, './base.html')
        
    context={
            'form':form
    }
    return render(request, 'register.html', context)


def delete(request,pk):
    person=Personne.objects.get(id=pk)
    person.delete()
    return redirect('/')
  
