from django.shortcuts import render, redirect
from .models import Denuncia
from .forms import DenunciaForm


def list_denuncia(request):
    denuncias = Denuncia.objects.all()
    return render(request, 'denuncia.html', {'denuncia': denuncias})

def create_denuncia(request):
    form = DenunciaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_denuncia')

    return render(request, 'denuncia-form.html', {'form': form})


def update_denuncia(request, id):
    denuncia = Denuncia.objects.get(id=id)
    form = DenunciaForm(request.POST or None, instance=denuncia)

    if form.is_valid():
        form.save()
        return redirect('list_denuncia')

    return render(request, 'atualizar.html', {'form': form, 'denuncia': denuncia})


def delete_denuncia(request, id):
    denuncia = Denuncia .objects.get(id=id)

    if request.method == 'POST':
        denuncia.delete()
        return redirect('list_denuncia')

    return render(request, 'denuncia-delete-confirm.html', {'denuncia': denuncia})

# Create your views here.

