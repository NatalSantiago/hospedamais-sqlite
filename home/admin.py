from django.contrib import admin

# Register your models here.
from home.models import hospedes,Empresa,PerfilUsuario,apartamentos,ItensConsumo,MovimentosAparts

admin.site.register(Empresa)
admin.site.register(hospedes)
admin.site.register(apartamentos)
admin.site.register(ItensConsumo)
admin.site.register(PerfilUsuario)
admin.site.register(MovimentosAparts)