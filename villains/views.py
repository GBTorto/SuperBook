from django.shortcuts import render

# Create your views here.
# villains/views.py

def lista_viloes(request):
    return render(request, 'villains/lista_viloes.html')

