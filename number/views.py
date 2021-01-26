from django.shortcuts import render
from .number_generator import MY_NUMBER


def index(request):
    context = {'num': MY_NUMBER[0]}
    return render(request, 'index.html', context)
