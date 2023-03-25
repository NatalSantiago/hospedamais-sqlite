# Generated by Django 4.1.7 on 2023-03-25 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_movimentosaparts_forma_pagamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartamentos',
            name='tipostatus',
            field=models.CharField(choices=[('Livre', 'Livre'), ('Ocupado', 'Ocupado'), ('Reservado', 'Reservado'), ('Em manutenção', 'Em manutenção'), ('Em limpeza', 'Em limpeza'), ('Outro', 'Outro')], max_length=50, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='tipodocindentificacao',
            field=models.CharField(blank=True, choices=[('Carteira de indentidade', 'Carteira de indentidade'), ('Carteira de motorista', 'Carteira de motorista'), ('Carteira de ind. Estrangeira', 'Carteira de ind. Estrangeira'), ('Passaporte', 'Passaporte'), ('Certidção de Nascimento', 'Certidção de Nascimento')], max_length=50, verbose_name='Documento de indentificação'),
        ),
    ]
