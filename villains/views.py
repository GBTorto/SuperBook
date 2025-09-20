from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Villain
from .forms import VillainForm
from django.urls import reverse_lazy

# Create your views here.
# villains/views.py

def lista_viloes(request):
    return render(request, 'villains/lista_viloes.html')

class ViloesListView(ListView):
    model = Villain
    template_name = 'villains/lista_viloes.html'
    context_object_name = 'villains'

class ViloesCreateView(CreateView):
    model = Villain
    form_class = VillainForm
    template_name = 'villains/form_viloes.html'
    success_url = reverse_lazy('lista_viloes')

class ViloesUpdateView(UpdateView):
    model = Villain
    form_class = VillainForm
    template_name = 'villains/form_viloes.html'
    success_url = reverse_lazy('lista_viloes')

class ViloesDeleteView(DeleteView):
    model = Villain
    template_name = 'villains/confirmar_exclusao.html'
    success_url = reverse_lazy('lista_viloes')