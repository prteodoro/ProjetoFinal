from django.contrib import admin
from .models import (
    Marca,
    Veiculo,
    Pessoa,
    Parametros,
    MovRotativo,
    Mensalista,
    MovMensalista
    )


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        "checkin", "checkout", "valor_hora", "veiculo", "horas_total", "total", "pago")
    


class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ("mensalista", "dt_pgto", "total")



admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
