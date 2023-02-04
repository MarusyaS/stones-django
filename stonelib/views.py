from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Inscription, Site


def index(request):
    insc_list = Inscription.objects.all()
    template = loader.get_template('stonelib/index.html')
    context = {
        'insc_list': insc_list,
    }
    return HttpResponse(template.render(context, request))

def single_inscription(request, ID):
    
    single_inscription = Inscription.objects.get(ID=ID)

    context = {'inscription': single_inscription}
    
    return render(request, 'stonelib/single_inscription.html', context)