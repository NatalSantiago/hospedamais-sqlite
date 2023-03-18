from django.contrib import admin

# Register your models here.
from home.models import hospedes,Empresa,PerfilUsuario,apartamentos

admin.site.register(Empresa)
admin.site.register(hospedes)
admin.site.register(apartamentos)
admin.site.register(PerfilUsuario)