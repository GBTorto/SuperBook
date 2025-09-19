# villains/urls.py
from django.urls import path
from . import views
from .views import ViloesCreateView, ViloesListView, ViloesUpdateView

urlpatterns = [
    path('', ViloesListView.as_view(), name='lista_viloes'),
    path('form_viloes/', ViloesCreateView.as_view(), name='form_viloes'),
    path('<int:pk>/editar/', ViloesUpdateView.as_view(), name='editar_viloes')
]

