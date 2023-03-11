from django.contrib import admin

# Register your models here.
from home.models import hospedes,Empresa,PerfilUsuario

admin.site.register(Empresa)
admin.site.register(hospedes)
admin.site.register(PerfilUsuario)