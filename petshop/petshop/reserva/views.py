from django.shortcuts import render
from reserva.forms import reservaform

def criar_reserva(request):
    form = reservaform(request.POST or None)
    sucesso = False
    if form.is_valid():
        form.save()
        sucesso = True
    contexto = {
        'form':form,
        'sucesso': sucesso
    }
    return render(request,'criar_reserva.html',contexto)

