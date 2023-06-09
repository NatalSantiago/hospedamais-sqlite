# Generated by Django 4.1.7 on 2023-03-24 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_itensconsumo_margemlucro'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimentosAparts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_checkin', models.DateField(blank=True, null=True, verbose_name='Data de CheckIn')),
                ('hora_checkin', models.TimeField(blank=True, null=True, verbose_name='Hora de CheckIn')),
                ('data_checkout', models.DateField(blank=True, null=True, verbose_name='Data de CheckOut')),
                ('hora_checkout', models.TimeField(blank=True, null=True, verbose_name='Hora de CheckOut')),
                ('qtd_hospedes', models.IntegerField(verbose_name='Nº. hóspedes')),
                ('qtd_excedentes', models.IntegerField(verbose_name='Excedentes')),
                ('valor_adiantamento', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Adiantamento')),
                ('valor_pago_excedente', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor por excedentes')),
                ('valor_consumo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor consumo')),
                ('forma_pagamento', models.CharField(choices=[('dinheiro', 'Dinheiro'), ('pix', 'PIX'), ('cartao_credito', 'Cartão de crédito'), ('cartao_debito', 'Cartão de débito'), ('transferencia_bancaria', 'Transferência bancária'), ('boleto_bancario', 'Boleto bancário'), ('cheque', 'Cheque'), ('paypal', 'PayPal'), ('cartao_refeicao', 'Cartão Refeição'), ('deposito', 'Depósito em conta'), ('credito_consumo', 'Crédito de Consumo'), ('voucher', 'Voucher'), ('outro', 'Outro')], max_length=25, verbose_name='Forma Pgto.')),
                ('data_fechamento', models.DateField(blank=True, null=True, verbose_name='Data fechamento')),
                ('hora_fechamento', models.TimeField(blank=True, null=True, verbose_name='Hora fechamento')),
                ('valor_total_conta', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Total')),
                ('valor_desconto', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Desconto')),
                ('valor_total_pago', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Líquido')),
                ('observacao', models.CharField(blank=True, max_length=255, null=True)),
                ('pago_sn', models.CharField(blank=True, max_length=1, null=True)),
                ('apartamento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.apartamentos')),
                ('empresa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.empresa')),
                ('hospede', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.hospedes')),
            ],
        ),
    ]
