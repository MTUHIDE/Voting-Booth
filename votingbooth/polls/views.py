from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    #template = loader.get_template('admin/index.html')
    context = {}

    return render(request, 'polls/index.html', context)
