from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User,AbstractUser

from django.db import models

from django import forms

from datetime import datetime

from bootstrap_datepicker_plus.widgets import DatePickerInput

# Create your models here.
class Empresa(models.Model):

    nome = models.CharField("Nome", max_length=150, unique=True, error_messages={'unique': "Empresa já cadastrada ! ! !", })
    email = models.EmailField(("Email"), max_length=254, unique=True, error_messages={'unique': "Email já cadastrado ! ! !", })
    fone = models.CharField(("Fone"), max_length=20)
    cnpj = models.CharField(max_length=18, unique=True, error_messages={'unique': "CNPJ já cadastrado ! ! !", })
    endereco = models.CharField(("Endereço"), max_length=100)
    cidade = models.CharField(("Cidade"), max_length=100)
    estado = models.CharField(("Estado"), max_length=2)
    Pais = models.CharField(("País"), max_length=100)

    def __str__(self):
        return self.nome


class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.get_username()} - {self.empresa.nome}"


class hospedes(models.Model):

    SEXOHOSPEDE = ( ("Masculino", "Masculino"), ("Femenino", "Femenino") )    

    TIPODOCINDENT = (("Carteira de indentidade", "Carteira de indentidade"),
                     ("Carteira de ind. Estrangeira", "Carteira de ind. Estrangeira"),
                     ("Passaporte", "Passaporte"), 
                     ("Certidção de Nascimento", "Certidção de Nascimento"))

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=False )
    nome = models.CharField("Nome", max_length=100, blank=True, null=False )
    email = models.EmailField(("Email"), max_length=254, blank=True, null=False )
    fone = models.CharField(("Fone"), max_length=25, blank=True, null=False )
    profissao = models.CharField(("Profissão/Ocupação"), max_length=100, blank=True, null=False )
    nacionalidade = models.CharField(("Nacionalidade"), max_length=100, blank=True, null=False )
    datanascimento = models.DateField(("Data Nascimento"), null=True, blank=True )
    generohospede = models.CharField(("Gênero"), max_length=10, choices=SEXOHOSPEDE, blank=True, null=False )
    cpf = models.CharField(max_length=14, blank=True, null=False)
    tipodocindentificacao = models.CharField(("Documento de indentificação"), max_length=50, blank=True, null=False, choices=TIPODOCINDENT)
    numerodocumento = models.CharField(("Número documento"), max_length=50, blank=True, null=False)
    orgaodocumento = models.CharField(("Orgão documento"), max_length=50, blank=True, null=False)
    endereco = models.CharField(("Endereço"), max_length=100, blank=True, null=False)
    cidade = models.CharField(("Cidade"), max_length=100, blank=True, null=False)
    estado = models.CharField(("Estado"), max_length=2, blank=True, null=False)
    Pais = models.CharField(("País"), max_length=100, blank=True, null=False)
    motviagemLazerferias = models.BooleanField(default=False, blank=True, null=False)
    motviagemCongressoFeira = models.BooleanField(default=False)
    motviagemEstudoCursos = models.BooleanField(default=False)
    motviagemNegocios = models.BooleanField(default=False)
    motviagemParentesAmigos = models.BooleanField(default=False)
    motviagemReligiao = models.BooleanField(default=False)
    motviagemCompras = models.BooleanField(default=False)
    motviagemOutros = models.BooleanField(default=False)
    meiotransporteAviao = models.BooleanField(default=False)
    meiotransporteCarro = models.BooleanField(default=False)
    meiotransporteOnibus = models.BooleanField(default=False)
    meiotransporteMoto = models.BooleanField(default=False)
    meiotransporteNavio = models.BooleanField(default=False)
    meiotransporteTrem = models.BooleanField(default=False)
    meiotransporteOutros = models.BooleanField(default=False)

    def __str__(self):
      return self.nome
    