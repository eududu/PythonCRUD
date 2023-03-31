from django.shortcuts import render, redirect
from app.form import PessoasForm
from app.models import Pessoas


def home(request):
    data={}
    data['db'] = Pessoas.objects.all()
    return render(request, 'index.html', data)

def forms(request):
    data = {}
    data['forms'] = PessoasForm()
    return render(request, 'forms.html', data)

def create(request):
    form = PessoasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data={}
    data['db']= Pessoas.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data={}
    data['db']= Pessoas.objects.get(pk=pk)
    data['forms']= PessoasForm(instance=data['db'])
    return render(request, 'forms.html', data)

def update(request, pk):
    data = {}
    data['db'] = Pessoas.objects.get(pk=pk)
    form = PessoasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Pessoas.objects.get(pk=pk)
    db.delete()
    return redirect('home')
    

# Create your views here.
