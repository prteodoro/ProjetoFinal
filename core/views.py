from django.shortcuts import render, redirect
from django.urls import reverse
from .models import (
    Pessoa,
    Veiculo,
    MovRotativo,
    Mensalista,
    MovMensalista
    )

from .forms import (
    PessoaForm,
    VeiculoForm,
    MovRotativoForm,
    MensalistaForm,
    MovMensalistaForm
    )


def home(request):
    context = {"mensagem": "Ola mundo"}
    return render(request, "base.html", context)


def lista_pessoas(request):
    pessoas = Pessoa.objects.all()
    form = PessoaForm()
    data = { "pessoas": pessoas, "form": form }
    return render(request, "core/lista_pessoas.html", data)


def pessoa_novo(request):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect(reverse("core:core_lista_pessoas"))


def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    form = VeiculoForm()
    data = { "veiculos": veiculos, "form": form }
    return render(request, "core/lista_veiculos.html", data)


def veiculo_novo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect(reverse("core:core_lista_veiculos"))


def lista_movrotativos(request):
    mov_rot = MovRotativo.objects.all()
    form = MovRotativoForm()
    data = {"mov_rot": mov_rot, "form": form }
    return render(
        request, "core/lista_movrotativos.html", data)


def movrotativos_novo(request):
    form = MovRotativoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect(reverse("core:core_lista_movrotativos"))


def lista_mensalistas(request):
    mensalistas = Mensalista.objects.all()
    form = MensalistaForm()
    data = { "mensalistas": mensalistas, "form": form }
    return render(
        request, "core/lista_mensalistas.html", data)


def mensalista_novo(request):
    form = MensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect(reverse("core:core_lista_mensalistas"))


def lista_movmensalistas(request):
    mov_mensalistas = MovMensalista.objects.all()
    form = MovMensalistaForm()
    data = { "mov_mensalistas": mov_mensalistas, "form": form }
    return render(
        request, "core/lista_movmensalistas.html", data)


def movmensalista_novo(request):
    form = MovMensalistaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect(reverse("core:core_lista_movmensalistas"))
