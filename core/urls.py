from django.urls import path, include

from .views import (
    home,
    lista_pessoas,
    lista_veiculos,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo,
    veiculo_novo,
    movrotativos_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update
    )


app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("pessoas/", lista_pessoas, name="core_lista_pessoas"),
    path("pessoa-novo/", pessoa_novo, name="core_pessoa_novo"),
    path("pessoa-update/<int:id>/", pessoa_update, name="core_pessoa_update"),

    path("veiculos/", lista_veiculos, name="core_lista_veiculos"),
    path("veiculo-novo/", veiculo_novo, name="core_veiculo_novo"),
    path("veiculo-update/<int:id>/", veiculo_update, name="core_veiculo_update"),

    path("mov-rot/", lista_movrotativos, name="core_lista_movrotativos"),
    path("mov-rot-novo/", movrotativos_novo, name="core_movrotativos_novo"),

    path("mensalistas/", lista_mensalistas, name="core_lista_mensalistas"),
    path("mensalista-novo/", mensalista_novo, name="core_mensalista_novo"),

    path("mov-mensal/", lista_movmensalistas,
         name="core_lista_movmensalistas"),
    path("mov-mensal-novo/", movmensalista_novo,
         name="core_movmensalista_novo")
]
