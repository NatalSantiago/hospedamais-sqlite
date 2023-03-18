# Generated by Django 4.1.7 on 2023-03-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_apartamentos_valordiaria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartamentos',
            name='tipoapart',
            field=models.CharField(choices=[('Simples', 'Simples'), ('Stander', 'Stander'), ('Luxo', 'Luxo'), ('Super Luxo', 'Super Luxo'), ('Duplex', 'Duplex'), ('Cobertura', 'Cobertura'), ('Loft', 'Loft'), ('Rústico', 'Rústico')], max_length=50, verbose_name='Tipo'),
        ),
    ]
