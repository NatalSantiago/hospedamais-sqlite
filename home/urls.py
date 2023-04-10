from django.urls import path

from .import views

from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from .views import PaginaInicial

from .views import itensConsumo_check_description,verificaSeHospedeExite,verificaSeApartamentoExite

from .views import delete_item_consumo_apart

urlpatterns = [

    path('', PaginaInicial.as_view(), name='inicio'),

    path('apartHome/', views.ApartHome_list, name='apartHome'),

    path('hospedes/', views.hospedes_list, name='hospedes'),

    path('hospedes/add/', views.hospedes_add, name='hospedes_add'),

    path('hospedes/edit/<int:hospede_pk>', views.hospedes_edit, name='hospedes_edit'),

    path('hospedes/delete/<int:hospede_pk>',views.hospedes_delete, name='hospedes_delete'),

    path('hospedes/verificaSeHospedeExite/', verificaSeHospedeExite, name='verificaSeHospedeExite'),

    path('login', auth_views.LoginView.as_view(template_name="home/login.html", redirect_authenticated_user=True), name='login'),

    path('userlogin', views.login_user, name="login-user"),

    path('logout', views.logoutuser, name='logout'),

    path('apartamentos/', views.apartamento_list, name='apartamentos'),

    path('apartamentos/add/', views.apartamentos_add, name='apartamentos_add'),

    path('apartamentos/edit/<int:apartamento_pk>', views.apartamentos_edit, name='apartamentos_edit'),

    path('apartamentos/delete/<int:apartamento_pk>',views.apartamentos_delete, name='apartamentos_delete'),

    path('apartamentos/verificaSeApartamentoExite/', verificaSeApartamentoExite, name='verificaSeApartamentoExite'),

    path('',views.apartamentos_erro, name='apartamentos_erro'),

    path('itensConsumo/', views.itensConsumo_list, name='itensConsumo'),

    path('itensConsumo/add/', views.itensConsumo_add, name='itensConsumo_add'),

    path('itensConsumo/edit/<int:itenConsumo_pk>', views.itensConsumo_edit, name='itensConsumo_edit'),

    path('itensConsumo/delete/<int:itenConsumo_pk>',views.itensConsumo_delete, name='itensConsumo_delete'),

    path('itensConsumo/check_description/', itensConsumo_check_description, name='itensConsumo_check_description'),
    
    path('salvar_variaveis/', views.salvar_variaveis, name='salvar_variaveis'),    
    
    path('itens_consumo_aparts/<int:apartamento_id>/', views.itens_consumo_aparts_apartamento, name='itens_consumo_aparts_apartamento'),

    path('LancarNovoItemHospede/<int:movID>/', views.LancarNovoItemHospede, name='LancarNovoItemHospede'),

    path('delete_item_consumo_apart/<int:item_pk>/', delete_item_consumo_apart, name='delete_item_consumo_apart'),

    path('caminho/para/get_preco_itemconsumo/<str:descricao>/', views.get_preco_itemconsumo_by_descricao, name='get_preco_itemconsumo_by_descricao'),

    path('buscar_apartamento/', views.buscar_apartamento, name='buscar_apartamento'),

    path('buscar_reservas/', views.buscar_reservas, name='buscar_reservas'),

    path('SalvarCheckIn/', views.SalvarCheckIn, name='SalvarCheckIn'),

    path('ConfirmarCancelarReserva/', views.ConfirmarCancelarReserva, name='ConfirmarCancelarReserva'),

    path('apartamento/<int:pk>/liberar/', views.liberar_apartamento, name='liberar_apartamento'),

    path('apartamento/<str:descApart>/cancelar_reserva/', views.cancelar_reserva, name='cancelar_reserva'),

]