from django.contrib import admin

from .models import Veicolo


class VeicoloAdmin(admin.ModelAdmin):
    pass


admin.site.register(Veicolo, VeicoloAdmin)

