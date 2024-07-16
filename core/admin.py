from django.contrib import admin
from .models import (
    Marca,
    Veiculo,
    Pessoa,
    Parametros,
    MovRotativo
    )


class MovRotativoAdmin(admin.ModelAdmin):
    list_display = (
        "checkin", "checkout", "valor_hora", "veiculo", "horas_total", "total", "pago")



admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovRotativo, MovRotativoAdmin)
