from django.template import loader
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Material
from django.views import generic


"""class IndexView(generic.ListView):
    template_name = 'devcart/index.html'
    def get_queryset(self):
        return Material.objects.all()"""


class IndexView(generic.ListView):
    model=Material
    template_name = 'devcart/index.html'
    def get_queryset(self):
        return Material.objects.all()
