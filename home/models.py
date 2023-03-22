from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

from django.db import models

from cpf_field.models import CPFField

from django import forms

from datetime import datetime

from bootstrap_datepicker_plus.widgets import DatePickerInput

from django.core.exceptions import ValidationError

import locale

# Create your models here.
class Empresa(models.Model):

    TIPOPLANO = (("Chumbo", "Chumbo"),    # 01 até 10   - valor R$: 70,00 Mensal  / R$: 588,00 Anual
                ("Zinco", "Zinco"),       # 11 até 20   - valor R$: 95,00 Mensal  / R$: 798,00 Anual
                ("Alumínio", "Alumínio"), # 21 até 30   - valor R$: 120,00 Mensal / R$: 1.008,00 Anual
                ("Níquel", "Níquel"),     # 31 até 50   - valor R$: 170,00 Mensal / R$: 1.428,00 Anual
                ("Cobre", "Cobre"),       # 51 até 80   - valor R$: 230,00 Mensal / R$: 1.932,00 Anual
                ("Prata", "Prata"),       # 81 até 100  - valor R$: 285,00 Mensal / R$: 2.394,00 Anual
                ("Paládio", "Paládio"),   # 101 até 130 - valor R$: 345,00 Mensal / R$: 2.898,00 Anual
                ("Ouro", "Ouro"),         # 131 até 150 - valor R$: 400,00 Mensal / R$: 3.360,00 Anual
                ("Platina", "Platina"),   # 151 até 200 - valor R$: 490,00 Mensal / R$: 4.116,00 Anual
                ("Ródio", "Ródio"))       # 201 até 300 - valor R$: 600,00 Mensal / R$: 5.040,00 Anual


    nome = models.CharField("Nome", max_length=150, unique=True, error_messages={'unique': "Empresa já cadastrada ! ! !", })
    email = models.EmailField(("Email"), max_length=254, unique=True, error_messages={'unique': "Email já cadastrado ! ! !", })
    fone = models.CharField(("Fone"), max_length=20)
    cnpj = models.CharField(max_length=18, unique=True, error_messages={'unique': "CNPJ já cadastrado ! ! !", })
    endereco = models.CharField(("Endereço"), max_length=100)
    cidade = models.CharField(("Cidade"), max_length=100)
    estado = models.CharField(("Estado"), max_length=2)
    Pais = models.CharField(("País"), max_length=100)
    tipoplano = models.CharField(("Tipo Plano"), max_length=20, choices=TIPOPLANO)


    def __str__(self):
        return f"{self.nome} - {self.tipoplano}"


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.get_username()} - {self.empresa.nome}"


class ItensConsumo(models.Model):

    TIPOUND = (("UND", "Unidade"),
              ("CX", "Caixa"),
              ("PCT", "Pacote"),
              ("KG", "Kilo"),
              ("DZ", "Duzia"),
              ("PC", "Peça"),
              ("LT", "Litro"))

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=False )
    descricao = models.CharField("Descrição", max_length=100, unique=True, error_messages={'unique': "Produto já cadastrado ! ! !", })
    unidade = models.CharField(("Unidade"), max_length=20, choices=TIPOUND)
    estoqueAtual = models.DecimalField(("Estoque Atual"), max_digits=10, decimal_places=2)
    precoCompra = models.DecimalField(("Preço Compra"), max_digits=10, decimal_places=2, blank=True, null=False)
    margemLucro = models.DecimalField(("Margem %"), max_digits=10, decimal_places=2, blank=True, null=False)
    precoVenda = models.DecimalField(("Preço Venda"), max_digits=10, decimal_places=2)
    observacao = models.CharField("Observação", max_length=100, blank=True, null=False)

    def __str__(self):
        return f"{self.descricao} - {self.unidade}"



class hospedes(models.Model):

    SEXOHOSPEDE = ( ("Masculino", "Masculino"), ("Femenino", "Femenino") )    

    TIPODOCINDENT = (("Carteira de indentidade", "Carteira de indentidade"),
                     ("Carteira de ind. Estrangeira", "Carteira de ind. Estrangeira"),
                     ("Passaporte", "Passaporte"), 
                     ("Certidção de Nascimento", "Certidção de Nascimento"))

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=False )
    nome = models.CharField("Nome", max_length=100, blank=True, null=False )
    cpf = CPFField('cpf', max_length=14, blank=True, null=False)
    datanascimento = models.DateField(("Data Nascimento"), null=True, blank=True )
    generohospede = models.CharField(("Gênero"), max_length=10, choices=SEXOHOSPEDE, blank=True, null=False )
    email = models.EmailField(("Email"), max_length=254, blank=True, null=False )
    fone = models.CharField(("Fone"), max_length=25, blank=True, null=False )
    profissao = models.CharField(("Profissão/Ocupação"), max_length=100, blank=True, null=False )
    nacionalidade = models.CharField(("Nacionalidade"), max_length=100, blank=True, null=False )
    endereco = models.CharField(("Endereço"), max_length=100, blank=True, null=False)
    cidade = models.CharField(("Cidade"), max_length=100, blank=True, null=False)
    estado = models.CharField(("Estado"), max_length=2, blank=True, null=False)
    Pais = models.CharField(("País"), max_length=100, blank=True, null=False)
    tipodocindentificacao = models.CharField(("Documento de indentificação"), max_length=50, blank=True, null=False, choices=TIPODOCINDENT)
    numerodocumento = models.CharField(("Número documento"), max_length=50, blank=True, null=False)
    orgaodocumento = models.CharField(("Orgão documento"), max_length=50, blank=True, null=False)
    motviagemLazerferias = models.BooleanField(("Férias/Lazer"), default=False, blank=True, null=False)
    motviagemCongressoFeira = models.BooleanField(("Congresso/Feira"), default=False)
    motviagemEstudoCursos = models.BooleanField(("Estudo/Cursos"), default=False)
    motviagemNegocios = models.BooleanField(("Negócios"), default=False)
    motviagemParentesAmigos = models.BooleanField(("Parentes/Amigos"), default=False)
    motviagemReligiao = models.BooleanField(("Religião"), default=False)
    motviagemCompras = models.BooleanField(("Compras"), default=False)
    motviagemOutros = models.BooleanField(("Outros"), default=False)
    meiotransporteAviao = models.BooleanField(("Avião"), default=False)
    meiotransporteCarro = models.BooleanField(("Carro"), default=False)
    meiotransporteOnibus = models.BooleanField(("Ônibus"), default=False)
    meiotransporteMoto = models.BooleanField(("Moto"), default=False)
    meiotransporteNavio = models.BooleanField(("Navio"), default=False)
    meiotransporteTrem = models.BooleanField(("Trem"), default=False)
    meiotransporteOutros = models.BooleanField(("Outros"), default=False)

    def __str__(self):
      return self.nome
    


class apartamentos(models.Model):

    TIPOAPART = ( ("Simples", "Simples"), ("Stander", "Stander"), ("Luxo", "Luxo"), ("Super Luxo", "Super Luxo"), ("Duplex", "Duplex"), ("Cobertura", "Cobertura"), ("Loft", "Loft"), ("Rústico", "Rústico"))    

    TIPOSTATUS = ( ("Livre", "Livre"), ("Ocupado", "Ocupado"), ("Reservado", "Reservado"), ("Em manutenção", "Em manutenção"), ("Outro", "Outro") )    


    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=False )
    descricao = models.CharField("Descrição", max_length=50, blank=True, null=False )
    tipoapart = models.CharField(("Tipo"), max_length=50, choices=TIPOAPART)
    ramal = models.CharField(("Ramal"), max_length=10, blank=True, null=False )
    valordiaria = models.DecimalField(("Valor da diária"), max_digits=10, decimal_places=2)
    observacao = models.CharField(("Observação"), max_length=255, blank=True, null=False )
    tipostatus = models.CharField(("Tipo"), max_length=50, choices=TIPOSTATUS)


    def __str__(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return f"{self.descricao} - Valor da diário R$ {locale.currency(self.valordiaria, grouping=True)}"
