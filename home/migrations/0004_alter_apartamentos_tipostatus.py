# Generated by Django 4.1.7 on 2023-03-23 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_apartamentos_qtdpessoas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartamentos',
            name='tipostatus',
            field=models.CharField(choices=[('Livre', 'Livre'), ('Ocupado', 'Ocupado'), ('Reservado', 'Reservado'), ('Em manutenção', 'Em manutenção'), ('Outro', 'Outro')], max_length=50, verbose_name='Status'),
        ),
    ]
