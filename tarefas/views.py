from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    if request.method == "POST":
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        Tarefa.objects.create(titulo=titulo, descricao=descricao)
        return redirect('lista_tarefas')
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

def apagar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('lista_tarefas') 
