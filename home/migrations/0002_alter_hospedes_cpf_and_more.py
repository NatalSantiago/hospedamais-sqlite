# Generated by Django 4.1.7 on 2023-03-15 23:58

import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospedes',
            name='cpf',
            field=cpf_field.models.CPFField(blank=True, max_length=14, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='meiotransporteAviao',
            field=models.BooleanField(default=False, verbose_name='Avião'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='meiotransporteCarro',
            field=models.BooleanField(default=False, verbose_name='Carro'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='meiotransporteMoto',
            field=models.BooleanField(default=False, verbose_name='Moto'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='meiotransporteNavio',
            field=models.BooleanField(default=False, verbose_name='Navio'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='meiotransporteOnibus',
            field=models.BooleanField(default=False, verbose_name='Ônibus'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='meiotransporteOutros',
            field=models.BooleanField(default=False, verbose_name='Outros'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='meiotransporteTrem',
            field=models.BooleanField(default=False, verbose_name='Trem'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='motviagemCompras',
            field=models.BooleanField(default=False, verbose_name='Compras'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='motviagemCongressoFeira',
            field=models.BooleanField(default=False, verbose_name='Congresso/Feira'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='motviagemEstudoCursos',
            field=models.BooleanField(default=False, verbose_name='Estudo/Cursos'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='motviagemLazerferias',
            field=models.BooleanField(blank=True, default=False, verbose_name='Férias/Lazer'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='motviagemNegocios',
            field=models.BooleanField(default=False, verbose_name='Negócios'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='motviagemOutros',
            field=models.BooleanField(default=False, verbose_name='Outros'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='motviagemParentesAmigos',
            field=models.BooleanField(default=False, verbose_name='Parentes/Amigos'),
        ),
        migrations.AlterField(
            model_name='hospedes',
            name='motviagemReligiao',
            field=models.BooleanField(default=False, verbose_name='Religião'),
        ),
    ]
