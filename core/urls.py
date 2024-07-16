from django.urls import path, include

from .views import home, lista_pessoas

app_name = "core"
urlpatterns = [
    path("", home, name="home"),
    path("pessoas/", lista_pessoas, name="core_lista_pessoas")
]
