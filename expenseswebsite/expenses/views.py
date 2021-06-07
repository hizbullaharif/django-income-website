from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def addexpenses(request):
    return render(request, 'addexpenses.html')
