from django.contrib import admin
from .models import Moto

# Register your models here.
class MotoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Moto, MotoAdmin)