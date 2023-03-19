from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect, render

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

import json

from home.models import PerfilUsuario,hospedes,apartamentos

from home.forms import HospedesForm,ApartamentosForm

class TabelaClientes(TemplateView):
    template_name = 'home/tabela.html'

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

    return render(request, 'home/hospedes.html', context)

################### Adicionar Hospedes ###################

@login_required
def hospedes_add(request):
    form = HospedesForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            # Verifica se o hóspede já existe
            nome = form.cleaned_data.get('nome')
            if not nome:
                form.add_error('nome', 'O campo nome é obrigatório.')
            else:
                cpf = form.cleaned_data.get('cpf')
                empresa = request.user.perfilusuario.empresa

                hospede_existente = hospedes.objects.filter(nome=nome, empresa=empresa).first()

                if hospede_existente:
                    # Se o hóspede já existe com o nome informado, define a instância do formulário para a instância do hóspede encontrado e redireciona para a página de edição
                    form = HospedesForm(instance=hospede_existente)
                    return redirect('hospedes_edit', hospede_pk=hospede_existente.pk)
                elif cpf != '':
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
                        return redirect('hospedes')
                else:
                    # Se o hóspede não existe e o CPF não foi informado ou não foi encontrado com outro nome, salva o novo registro
                    hospede = form.save(commit=False)
                    hospede.empresa = empresa
                    hospede.save()
                    return redirect('hospedes')

    nome_empresa = None
    empresa_iduser = None

    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
    except PerfilUsuario.DoesNotExist:
        pass

    context = {
        'form': form,
        'nome_empresa': nome_empresa,
        'empresa_iduser': empresa_iduser
    }

    return render(request, 'home/hospedes_add.html', context)


################### Editar Hospedes ###################

@login_required
def hospedes_edit(request, hospede_pk):
    hospedeEdit = hospedes.objects.get(pk=hospede_pk)

    form = HospedesForm(request.POST or None, instance=hospedeEdit)

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

    nome_empresa = None
    empresa_iduser = None

    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
    except PerfilUsuario.DoesNotExist:
        pass

    context = {
        'form': form,
        'nome_empresa': nome_empresa,
        'empresa_iduser': empresa_iduser
    }

    return render(request, 'home/hospedes_edit.html', context)

################### Exclusão de Clientes ###################

@login_required
def hospedes_delete(request, hospede_pk):
    hospedeDelete = hospedes.objects.get(pk=hospede_pk)

    nome_empresa = None
    empresa_iduser = None

    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
    except PerfilUsuario.DoesNotExist:
        pass

    if request.POST:
        hospedeDelete.delete()
        return redirect('hospedes')
    context = {
        'hospede': hospedeDelete.id,
        'hospedeNome': hospedeDelete.nome,
        'nome_empresa': empresa.nome,
        'empresa_iduser': perfil_usuario.empresa.pk

    }            
    return render(request, 'home/hospedes_delete.html', context )

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

    return render(request, 'home/apartamentos.html', context)


################### Adicionar Apartamentos ###################

@login_required
def apartamentos_add(request):
    form = ApartamentosForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            # Verifica se o apartamento já existe
            descricao = form.cleaned_data.get('descricao')
            if not descricao:
                form.add_error('descricao', 'O campo descrição é obrigatório.')
            else:
                empresa = request.user.perfilusuario.empresa
                apart_existente = apartamentos.objects.filter(descricao=descricao, empresa=empresa).first()

                if apart_existente:
                    # Se o apartamento já existe com o nome informado, define a instância do formulário para a instância do hóspede encontrado e redireciona para a página de edição
                    form = ApartamentosForm(instance=apart_existente)
                    return redirect('apartamentos_edit', apartamento_pk=apart_existente.pk)
                else:
                    # Se o hóspede não existe e o CPF não foi informado ou não foi encontrado com outro nome, salva o novo registro
                    apartamento = form.save(commit=False)
                    apartamento.empresa = empresa
                    apartamento.save()
                    return redirect('apartamentos')

    nome_empresa = None
    empresa_iduser = None

    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
    except PerfilUsuario.DoesNotExist:
        pass

    context = {
        'form': form,
        'nome_empresa': nome_empresa,
        'empresa_iduser': empresa_iduser
    }

    return render(request, 'home/apartamentos_add.html', context)


################### Editar Apartamentos ###################

@login_required
def apartamentos_edit(request, apartamento_pk):
    apartamentoEdit = apartamentos.objects.get(pk=apartamento_pk)

    form = ApartamentosForm(request.POST or None, instance=apartamentoEdit)

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

    nome_empresa = None
    empresa_iduser = None

    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
    except PerfilUsuario.DoesNotExist:
        pass

    context = {
        'form': form,
        'nome_empresa': nome_empresa,
        'empresa_iduser': empresa_iduser
    }

    return render(request, 'home/apartamentos_edit.html', context)


################### Exclusão de Apartamentos ###################

@login_required
def apartamentos_delete(request, apartamento_pk):
    apartamentoDelete = apartamentos.objects.get(pk=apartamento_pk)

    nome_empresa = None
    empresa_iduser = None

    try:
        perfil_usuario = request.user.perfilusuario
        empresa = perfil_usuario.empresa
        nome_empresa = empresa.nome
        empresa_iduser = perfil_usuario.empresa.pk
    except PerfilUsuario.DoesNotExist:
        pass

    if request.POST:
        apartamentoDelete.delete()
        return redirect('apartamentos')
    context = {
        'apartamento': apartamentoDelete.id,
        'apartamentodescricao': apartamentoDelete.descricao,
        'nome_empresa': empresa.nome,
        'empresa_iduser': perfil_usuario.empresa.pk

    }            
    return render(request, 'home/apartamentos_delete.html', context )


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

    return render(request, 'home/apartsHome.html', context)
