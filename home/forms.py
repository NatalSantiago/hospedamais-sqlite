from django import forms

from home.models import hospedes,apartamentos,ItensConsumo,MovimentosAparts

from bootstrap_datepicker_plus.widgets import DatePickerInput

import re

import widget_tweaks 

class HospedesForm(forms.ModelForm):
    class Meta:
       model = hospedes
       fields = ["nome,cpf,datanascimento,generohospede,email,fone"]
       widgets = {
           "datanascimento": DatePickerInput(options={"format": "DD/MM/YYYY"}),
        }
       
       fields = '__all__'

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()
    
    def clean_email(self):
        email = self.cleaned_data['email']
        return email.lower()    
    
    def clean_cpf(self):
       cpf = self.cleaned_data['cpf']
       if cpf:
           cpf_numeros = re.sub('[^0-9]', '', cpf)  # remove caracteres não numéricos
           cpf_formatado = f'{cpf_numeros[:3]}.{cpf_numeros[3:6]}.{cpf_numeros[6:9]}-{cpf_numeros[9:11]}'  # formata CPF
           return cpf_formatado
       else:
           return ''
       


class ApartamentosForm(forms.ModelForm):
    class Meta:
       model = apartamentos
       
       fields = '__all__'

    def clean_descricao(self):
        nome = self.cleaned_data['descricao']
        return nome.upper()

class ItensConsumoForm(forms.ModelForm):
    class Meta:
      model = ItensConsumo

      fields = '__all__'

    def clean_descricao(self):
        nome = self.cleaned_data['descricao']
        return nome.upper()


