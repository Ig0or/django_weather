from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .services import *
from .key import key

# Create your views here.

cidades = []
def index(request):
    if request.method == 'POST':
        retorno = request.POST['cidade']
        if retorno:
            cidade_nova = consulta_api(retorno, key)
            if type(cidade_nova) == dict:
                cidades.insert(0, cidade_nova)
                return redirect('index')
        else:
            return redirect('index')
    return render(request, 'app/index.html', {'cidades': cidades})

def reset(request):
    global cidades
    cidades = []
    return redirect("index")

