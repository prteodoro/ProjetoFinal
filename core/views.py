from django.shortcuts import render


def home(request):
    context = {"mensagem": "Ola mundo"}
    return render(request, "base.html", context)
