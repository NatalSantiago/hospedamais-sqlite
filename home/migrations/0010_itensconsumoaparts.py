# Generated by Django 4.1.7 on 2023-03-25 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_apartamentos_tipostatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItensConsumoAparts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_lancamento', models.DateField(blank=True, null=True, verbose_name='Data lançamento')),
                ('hora_lancamento', models.TimeField(blank=True, null=True, verbose_name='Hora lançamento')),
                ('preco_item', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Preço')),
                ('qtd_lancamento', models.IntegerField(verbose_name='Qtd.')),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Total')),
                ('apartamento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.apartamentos')),
                ('empresa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.empresa')),
                ('hospede', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.hospedes')),
                ('item_lancamento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.itensconsumo')),
                ('movimento', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.movimentosaparts')),
            ],
        ),
    ]