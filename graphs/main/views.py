from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def param(request):
    return render(request, 'main/params.html')

def visual(request):
    return render(request, 'main/visual.html')
