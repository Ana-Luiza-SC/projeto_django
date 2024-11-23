from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('apagar_tarefa/<int:id>/', views.apagar_tarefa, name='apagar_tarefa'),
]
