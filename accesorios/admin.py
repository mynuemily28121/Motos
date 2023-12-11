from django.contrib import admin
from .models import CategoriaAcc, Accesorio

# Register your models here.
class CategoriaAccAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class AccesorioAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(CategoriaAcc, CategoriaAccAdmin)
admin.site.register(Accesorio, AccesorioAdmin)