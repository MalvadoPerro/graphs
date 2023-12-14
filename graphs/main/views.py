from django.shortcuts import render, redirect
from django.template.defaulttags import register
from .models import Count
from .forms import CountForm, NamesForm

@register.filter
def get_range(value):
    return range(1, value + 1)

def index(request):
    if request.method == 'POST':
        form = CountForm(request.POST)
        form.save()
        return redirect('params')

    form = CountForm()

    data = {
        'form': form
    }

    return render(request, 'main/index.html', data)

def param(request):
    cont = Count.objects.all()[:1]

    if request.method == 'POST':
        form_name = NamesForm(request.POST)
        form_name.save()

    form_name = NamesForm()

    data = {
        'cont': cont,
        'form_name': form_name
    }

    return render(request, 'main/params.html', data)

def visual(request):
    return render(request, 'main/visual.html')
