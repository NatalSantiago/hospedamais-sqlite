from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

import json

from django.http import JsonResponse

from home.models import PerfilUsuario,hospedes,apartamentos,ItensConsumo

from home.forms import HospedesForm,ApartamentosForm,ItensConsumoForm

class PaginaInicial(LoginRequiredMixin, TemplateView):
    template_name = 'home/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            perfil_usuario = PerfilUsuario.objects.get(user=self.request.user.id)
            nome_empresa = perfil_usuario.empresa.nome
            empresa_iduser = perfil_usuario.empresa.pk
        except PerfilUsuario.DoesNotExist:
            nome_empresa = 'Nenhuma empresa vinculada'
            empresa_iduser = None
        context['nome_empresa'] = nome_empresa
        context['empresa_iduser'] = empresa_iduser
        return context
    
################### Listagem de Hospedes ###################

@login_required
def hospedes_list(request):
    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
        hospedeList = hospedes.objects.filter(empresa=empresa)
    except PerfilUsuario.DoesNotExist:
        empresa = None
        empresa_iduser = None
        nome_empresa = 'Mostrando os hospedes de todas a empresas'
        hospedeList = hospedes.objects.all()

    context = {
        'hospedes': hospedeList,
        'empresa': empresa,
        'empresa_iduser': empresa_iduser,
        'nome_empresa': nome_empresa
    }

    return render(request, 'home/hospedes/hospedes.html', context)

################### Adicionar Hospedes ###################

@login_required
def hospedes_add(request):
    form = HospedesForm(request.POST or None)
    action = '' # Inicializa a variável action com um valor padrão
    try:
       perfil_usuario = request.user.perfilusuario
       empresa = perfil_usuario.empresa
       nome_empresa = empresa.nome
       empresa_iduser = perfil_usuario.empresa.pk
       context = {
            'form': form,
            'nome_empresa': nome_empresa,
            'empresa_iduser': empresa_iduser
       }
    except PerfilUsuario.DoesNotExist:
        return redirect('hospedes')
    ###############################################################
    if request.POST:
        if form.is_valid():
            # Verifica se o hóspede já existe
            nome = form.cleaned_data.get('nome')
            if not nome:
                form.add_error('nome', 'O campo nome é obrigatório.')
            else:
                cpf = form.cleaned_data.get('cpf')
                empresa = request.user.perfilusuario.empresa
                if cpf != '':
                    # Verifica se o CPF já foi cadastrado com outro nome
                    cpf_existente = hospedes.objects.filter(cpf=cpf, empresa=empresa).exclude(nome=nome).first()

                    if cpf_existente:
                        # Se o CPF já foi cadastrado com outro nome, mostra uma mensagem de erro com o nome do hóspede
                        form.add_error('cpf', f"O CPF {cpf} já está cadastrado para o hóspede {cpf_existente.nome}.")
                    else:
                        # Se o hóspede não existe e o CPF não foi informado ou não foi encontrado com outro nome, salva o novo registro
                        hospede = form.save(commit=False)
                        hospede.empresa = empresa
                        hospede.save()
                        action = request.POST.get('action')
                        if action == 'save_exit':
                           return redirect('hospedes')
                        elif action == 'save_add':
                           return redirect('hospedes_add')
                else:
                    # Se o hóspede não existe e o CPF não foi informado ou não foi encontrado com outro nome, salva o novo registro
                    hospede = form.save(commit=False)
                    hospede.empresa = empresa
                    hospede.save()

                    action = request.POST.get('action')
                    if action == 'save_exit':
                       return redirect('hospedes')
                    elif action == 'save_add':
                       return redirect('hospedes_add')
                    
    return render(request, 'home/hospedes/hospedes_add.html', context)

################### Localizar hospede já cadastrado ###################

@login_required
def verificaSeHospedeExite(request):
    nome = request.POST.get('nome')

    nome_existente = hospedes.objects.filter(nome__iexact=nome).exists()

    if nome_existente:
        id_hospede = hospedes.objects.filter(nome__iexact=nome).values('id')[0]['id']
        return JsonResponse({'nome_existente': True, 'id': id_hospede})
    else:
        return JsonResponse({'nome_existente': False})


################### Editar Hospedes ###################

@login_required
def hospedes_edit(request, hospede_pk):
    hospedeEdit = hospedes.objects.get(pk=hospede_pk)
    form = HospedesForm(request.POST or None, instance=hospedeEdit)
    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
        context = {
          'form': form,
          'nome_empresa': nome_empresa,
          'empresa_iduser': empresa_iduser
        }
    except PerfilUsuario.DoesNotExist:
        return redirect('hospedes')

    if request.POST:
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            if not nome:
                form.add_error('nome', 'O campo nome é obrigatório.')
            else:
                hospede = form.save(commit=False)
                hospede.empresa = request.user.perfilusuario.empresa or None            
                hospede.save()
                return redirect('hospedes')

    return render(request, 'home/hospedes/hospedes_edit.html', context)

################### Exclusão de Clientes ###################

@login_required
def hospedes_delete(request, hospede_pk):
    hospedeDelete = hospedes.objects.get(pk=hospede_pk)
    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        context = {
          'emmpresa': empresa,
          'hospede': hospedeDelete.id,
          'hospedeNome': hospedeDelete.nome,
        }            
    except PerfilUsuario.DoesNotExist:
        return redirect('hospedes')

    if request.POST:
        hospedeDelete.delete()
        return redirect('hospedes')
    
    return render(request, 'home/hospedes/hospedes_delete.html', context )

###############################################################

def login_user(request):
    logout(request)
    resp = {"status": 'failed', 'msg': ''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status'] = 'success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp), content_type='application/json')

# Logout

def logoutuser(request):
    logout(request)
    return redirect('login')

################### Listagem de Apartamentos ###################

@login_required
def apartamento_list(request):
    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_plano = empresa.tipoplano
        empresa_iduser = perfil_usuario.empresa.pk
        qtdAparts = apartamentos.objects.filter(empresa=empresa).count()
        apartList = apartamentos.objects.filter(empresa=empresa)
    except PerfilUsuario.DoesNotExist:
        empresa = None
        empresa_iduser = None
        nome_empresa = 'Mostrando os apartamentos de todas a empresas'
        empresa_plano = None
        qtdAparts = None
        apartList = apartamentos.objects.all()

    context = {
        'apartamentos': apartList,
        'empresa': empresa,
        'empresa_iduser': empresa_iduser,
        'nome_empresa': nome_empresa,
        'empresa_plano': empresa_plano,
        'qtdAparts': qtdAparts
    }

    return render(request, 'home/apartamentos/apartamentos.html', context)


################### Adicionar Apartamentos ###################

@login_required
def apartamentos_add(request):
    form = ApartamentosForm(request.POST or None)
    action = '' # Inicializa a variável action com um valor padrão
    try:
       perfil_usuario = request.user.perfilusuario
       empresa = request.user.perfilusuario.empresa
       nome_empresa = empresa.nome
       empresa_iduser = perfil_usuario.empresa.pk
       empresa_plano = empresa.tipoplano
       qtdAparts = apartamentos.objects.filter(empresa=empresa).count()
       context = {
            'form': form,
            'perfil_usuario': perfil_usuario,
            'nome_empresa': nome_empresa,
            'empresa_iduser': empresa_iduser,
            'empresa_plano': empresa_plano,
            'qtdAparts': qtdAparts,
       }
    except PerfilUsuario.DoesNotExist:
        return redirect('apartamentos')
    ###############################################################
    ## Se o usuário tiver no limete do plano escolhido não o deixa incluir outro apartamento ##
    if empresa_plano == 'Chumbo' and qtdAparts >= 10:
       return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    elif empresa_plano == 'Zinco' and qtdAparts >= 20:
       return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    elif empresa_plano == 'Alumínio' and qtdAparts >= 30:
       return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    elif empresa_plano == 'Níquel' and qtdAparts >= 50:
       return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    elif empresa_plano == 'Cobre' and qtdAparts >= 80:
       return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    elif empresa_plano == 'Prata' and qtdAparts >= 100:
       return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    elif empresa_plano == 'Paládio' and qtdAparts >= 130:
           return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    elif empresa_plano == 'Ouro' and qtdAparts >= 150:
       return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    elif empresa_plano == 'Platina' and qtdAparts >= 200:
       return render(request, 'home/apartamentos/apartamentos_erro.html', context)
    #####################################################
    if request.POST:
        if form.is_valid():
            # Verifica se o apartamento já existe
            descricao = form.cleaned_data.get('descricao')
            if not descricao:
                form.add_error('descricao', 'O campo descrição é obrigatório.')
            else:
                empresa = request.user.perfilusuario.empresa
                # Se o hóspede não existe e o CPF não foi informado ou não foi encontrado com outro nome, salva o novo registro
                apartamento = form.save(commit=False)
                apartamento.empresa = empresa
                apartamento.save()
                action = request.POST.get('action')
                if action == 'save_exit':
                   return redirect('apartamentos')
                elif action == 'save_add':
                   return redirect('apartamentos_add')

    return render(request, 'home/apartamentos/apartamentos_add.html', context)

################### Localizar apartamento já cadastrado ###################

@login_required
def verificaSeApartamentoExite(request):
    descricao = request.POST.get('descricao')

    descricao_existente = apartamentos.objects.filter(descricao__iexact=descricao).exists()

    if descricao_existente:
        id_apartamento = apartamentos.objects.filter(descricao__iexact=descricao).values('id')[0]['id']
        return JsonResponse({'descricao_existente': True, 'id': id_apartamento})
    else:
        return JsonResponse({'descricao_existente': False})

################### Editar Apartamentos ###################

@login_required
def apartamentos_edit(request, apartamento_pk):
    apartamentoEdit = apartamentos.objects.get(pk=apartamento_pk)
    form = ApartamentosForm(request.POST or None, instance=apartamentoEdit)
    try:
       perfil_usuario = request.user.perfilusuario
       empresa = perfil_usuario.empresa
       nome_empresa = empresa.nome
       empresa_iduser = perfil_usuario.empresa.pk
       context = {
            'form': form,
            'perfil_usuario': perfil_usuario,
            'nome_empresa': nome_empresa,
            'empresa_iduser': empresa_iduser,
       }
    except PerfilUsuario.DoesNotExist:
        return redirect('apartamentos')

    if request.POST:
        if form.is_valid():
            descricao = form.cleaned_data.get('descricao')
            if not descricao:
                form.add_error('descricao', 'O campo descrição é obrigatório.')
            else:
                apartamento = form.save(commit=False)
                apartamento.empresa = request.user.perfilusuario.empresa or None            
                apartamento.save()
                return redirect('apartamentos')

    return render(request, 'home/apartamentos/apartamentos_edit.html', context)


################### Exclusão de Apartamentos ###################

@login_required
def apartamentos_delete(request, apartamento_pk):
    apartamentoDelete = apartamentos.objects.get(pk=apartamento_pk)
    try:
      perfil_usuario = request.user.perfilusuario
      empresa = perfil_usuario.empresa
      context = {
        'apartamento': apartamentoDelete.id,
        'apartamentodescricao': apartamentoDelete.descricao,
        'nome_empresa': empresa.nome,
        'empresa_iduser': perfil_usuario.empresa.pk
       }
    except PerfilUsuario.DoesNotExist:
        return redirect('apartamentos')
    ###############################################################
    if request.POST:
        apartamentoDelete.delete()
        return redirect('apartamentos')

    return render(request, 'home/apartamentos/apartamentos_delete.html', context )

################### Mensagem de erro qtd. aparts atingida  ###################

@login_required
def apartamentos_erro(request):

    empresa = request.user.perfilusuario.empresa
    nome_empresa = empresa.nome
    empresa_plano = empresa.tipoplano
    qtdAparts = apartamentos.objects.filter(empresa=empresa).count()

    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_plano = empresa.tipoplano
        qtdAparts = apartamentos.objects.filter(empresa=empresa).count()
    except PerfilUsuario.DoesNotExist:
        pass

    context = {
        'nome_empresa': nome_empresa,
        'empresa_plano': empresa_plano,
        'qtdAparts': qtdAparts,
    }            
    return render(request, 'home/apartamentos/apartamentos_erro.html', context )


################### Listagem de Apartamentos ###################

@login_required
def ApartHome_list(request):
    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
        apartList = apartamentos.objects.filter(empresa=empresa)
    except PerfilUsuario.DoesNotExist:
        empresa = None
        empresa_iduser = None
        nome_empresa = 'Mostrando os apartamentos de todas a empresas'
        apartList = apartamentos.objects.all()

    context = {
        'apartamentos': apartList,
        'empresa': empresa,
        'empresa_iduser': empresa_iduser,
        'nome_empresa': nome_empresa
    }

    return render(request, 'home/apartamentos/apartsHome.html', context)


################### Listagem de Itens de Consumo ###################

@login_required
def itensConsumo_list(request):
    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
        itenList = ItensConsumo.objects.filter(empresa=empresa)
    except PerfilUsuario.DoesNotExist:
        empresa = None
        empresa_iduser = None
        nome_empresa = 'Mostrando os itns de consumo de todas a empresas'
        itenList = apartamentos.objects.all()

    context = {
        'itensConsumo': itenList,
        'empresa': empresa,
        'empresa_iduser': empresa_iduser,
        'nome_empresa': nome_empresa,
    }

    return render(request, 'home/itensConsumo/itensConsumo.html', context)


################### Adicionar Itens Consumo ###################

@login_required
def itensConsumo_add(request):
    form = ItensConsumoForm(request.POST or None)
    action = '' # Inicializa a variável action com um valor padrão
    try:
       perfil_usuario = request.user.perfilusuario
       empresa = request.user.perfilusuario.empresa
       nome_empresa = empresa.nome
       empresa_iduser = perfil_usuario.empresa.pk
       context = {
            'form': form,
            'perfil_usuario': perfil_usuario,
            'nome_empresa': nome_empresa,
            'empresa_iduser': empresa_iduser,
       }
    except PerfilUsuario.DoesNotExist:
        return redirect('itensConsumo')
    #####################################################
    if request.POST:
        if form.is_valid():
            # Verifica se o apartamento já existe
            descricao = form.cleaned_data.get('descricao')
            if not descricao:
                form.add_error('descricao', 'O campo descrição é obrigatório.')
            else:
                empresa = request.user.perfilusuario.empresa
#                item_existente = ItensConsumo.objects.filter(descricao=descricao, empresa=empresa).first()
                # Se o hóspede não existe e o CPF não foi informado ou não foi encontrado com outro nome, salva o novo registro
                itemconsumo = form.save(commit=False)
                itemconsumo.empresa = empresa
                itemconsumo.save()
                action = request.POST.get('action')
                if action == 'save_exit':
                   return redirect('itensConsumo')
                elif action == 'save_add':
                   return redirect('itensConsumo_add')

    return render(request, 'home/itensConsumo/itensConsumo_add.html', context)


################### Localizar itens já cadastrados ###################

@login_required
def itensConsumo_check_description(request):
    descricao = request.POST.get('descricao')

    item_existente = ItensConsumo.objects.filter(descricao__iexact=descricao).exists()

    if item_existente:
        id_item = ItensConsumo.objects.filter(descricao__iexact=descricao).values('id')[0]['id']
        return JsonResponse({'item_existente': True, 'id': id_item})
    else:
        return JsonResponse({'item_existente': False})

################### Editar Apartamentos ###################

@login_required
def itensConsumo_edit(request, itenConsumo_pk):
    itenConsumoEdit = ItensConsumo.objects.get(pk=itenConsumo_pk)
    form = ItensConsumoForm(request.POST or None, instance=itenConsumoEdit)
    try:
       perfil_usuario = request.user.perfilusuario
       empresa = perfil_usuario.empresa
       nome_empresa = empresa.nome
       empresa_iduser = perfil_usuario.empresa.pk
       context = {
            'form': form,
            'perfil_usuario': perfil_usuario,
            'nome_empresa': nome_empresa,
            'empresa_iduser': empresa_iduser,
       }
    except PerfilUsuario.DoesNotExist:
        return redirect('itensConsumo')

    if request.POST:
        if form.is_valid():
            descricao = form.cleaned_data.get('descricao')
            if not descricao:
                form.add_error('descricao', 'O campo descrição é obrigatório.')
            else:
                itenConsumo = form.save(commit=False)
                itenConsumo.empresa = request.user.perfilusuario.empresa or None            
                itenConsumo.save()
                return redirect('itensConsumo')

    return render(request, 'home/itensConsumo/itensConsumo_edit.html', context)


################### Exclusão de Itens de Consumo ###################

@login_required
def itensConsumo_delete(request, itenConsumo_pk):
    itenConsumoDelete = ItensConsumo.objects.get(pk=itenConsumo_pk)
    try:
      perfil_usuario = request.user.perfilusuario
      empresa = perfil_usuario.empresa
      context = {
        'itenConsumo': itenConsumoDelete.id,
        'itenConsumodescricao': itenConsumoDelete.descricao,
        'nome_empresa': empresa.nome,
        'empresa_iduser': perfil_usuario.empresa.pk
       }
    except PerfilUsuario.DoesNotExist:
        return redirect('itensConsumo')
    ###############################################################
    if request.POST:
        itenConsumoDelete.delete()
        return redirect('itensConsumo')

    return render(request, 'home/itensConsumo/itensConsumo_delete.html', context )

