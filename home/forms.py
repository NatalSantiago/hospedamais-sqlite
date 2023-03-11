from django import forms

from home.models import hospedes

from bootstrap_datepicker_plus.widgets import DatePickerInput


class HospedesForm(forms.ModelForm):
    class Meta:
       model = hospedes

       fields = ["nome,cpf,datanascimento,generohospede,email,fone"]
       widgets = {
           "datanascimento": DatePickerInput(options={"format": "DD/MM/YYYY"}),
        }
       
       fields = '__all__'
