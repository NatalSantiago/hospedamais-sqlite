from django.urls import path

from .import views

from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

from .views import PaginaInicial

urlpatterns = [

    path('', PaginaInicial.as_view(), name='inicio'),

    path('hospedes/', views.hospedes_list, name='hospedes'),

    path('hospedes/add/', views.hospedes_add, name='hospedes_add'),

    path('hospedes/edit/<int:hospede_pk>', views.hospedes_edit, name='hospedes_edit'),

    path('hospedes/delete/<int:hospede_pk>',views.hospedes_delete, name='hospedes_delete'),

    path('login', auth_views.LoginView.as_view(template_name="home/login.html", redirect_authenticated_user=True), name='login'),

    path('userlogin', views.login_user, name="login-user"),

    path('logout', views.logoutuser, name='logout'),

    path('apartamentos/', views.apartamento_list, name='apartamentos'),

    path('apartamentos/add/', views.apartamentos_add, name='apartamentos_add'),

    path('apartamentos/edit/<int:apartamento_pk>', views.apartamentos_edit, name='apartamentos_edit'),

    path('apartamentos/delete/<int:apartamento_pk>',views.apartamentos_delete, name='apartamentos_delete'),

]
