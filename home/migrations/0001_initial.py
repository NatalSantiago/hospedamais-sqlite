# Generated by Django 4.1.7 on 2023-03-23 03:10

import cpf_field.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(error_messages={'unique': 'Empresa já cadastrada ! ! !'}, max_length=150, unique=True, verbose_name='Nome')),
                ('email', models.EmailField(error_messages={'unique': 'Email já cadastrado ! ! !'}, max_length=254, unique=True, verbose_name='Email')),
                ('fone', models.CharField(max_length=20, verbose_name='Fone')),
                ('cnpj', models.CharField(error_messages={'unique': 'CNPJ já cadastrado ! ! !'}, max_length=18, unique=True)),
                ('endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('Pais', models.CharField(max_length=100, verbose_name='País')),
                ('tipoplano', models.CharField(choices=[('Chumbo', 'Chumbo'), ('Zinco', 'Zinco'), ('Alumínio', 'Alumínio'), ('Níquel', 'Níquel'), ('Cobre', 'Cobre'), ('Prata', 'Prata'), ('Paládio', 'Paládio'), ('Ouro', 'Ouro'), ('Platina', 'Platina'), ('Ródio', 'Ródio')], max_length=20, verbose_name='Tipo Plano')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.empresa')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ItensConsumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(error_messages={'unique': 'Produto já cadastrado ! ! !'}, max_length=100, unique=True, verbose_name='Descrição')),
                ('unidade', models.CharField(choices=[('UND', 'Unidade'), ('CX', 'Caixa'), ('PCT', 'Pacote'), ('KG', 'Kilo'), ('DZ', 'Duzia'), ('PC', 'Peça'), ('LT', 'Litro'), ('SV', 'Serviço(s)')], max_length=20, verbose_name='Unidade')),
                ('estoqueMinimo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Estoque Mínimo')),
                ('estoqueAtual', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Estoque Atual')),
                ('precoCompra', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Preço Compra')),
                ('margemLucro', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Margem %')),
                ('precoVenda', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço Venda')),
                ('observacao', models.CharField(blank=True, max_length=100, verbose_name='Observação')),
                ('empresa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='hospedes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('cpf', cpf_field.models.CPFField(blank=True, max_length=14, verbose_name='cpf')),
                ('datanascimento', models.DateField(blank=True, null=True, verbose_name='Data Nascimento')),
                ('generohospede', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10, verbose_name='Gênero')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('fone', models.CharField(blank=True, max_length=25, verbose_name='Fone')),
                ('profissao', models.CharField(blank=True, max_length=100, verbose_name='Profissão/Ocupação')),
                ('nacionalidade', models.CharField(blank=True, max_length=100, verbose_name='Nacionalidade')),
                ('endereco', models.CharField(blank=True, max_length=100, verbose_name='Endereço')),
                ('cidade', models.CharField(blank=True, max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=2, verbose_name='Estado')),
                ('Pais', models.CharField(blank=True, max_length=100, verbose_name='País')),
                ('tipodocindentificacao', models.CharField(blank=True, choices=[('Carteira de indentidade', 'Carteira de indentidade'), ('Carteira de ind. Estrangeira', 'Carteira de ind. Estrangeira'), ('Passaporte', 'Passaporte'), ('Certidção de Nascimento', 'Certidção de Nascimento')], max_length=50, verbose_name='Documento de indentificação')),
                ('numerodocumento', models.CharField(blank=True, max_length=50, verbose_name='Número documento')),
                ('orgaodocumento', models.CharField(blank=True, max_length=50, verbose_name='Orgão documento')),
                ('motviagemLazerferias', models.BooleanField(blank=True, default=False, verbose_name='Férias/Lazer')),
                ('motviagemCongressoFeira', models.BooleanField(default=False, verbose_name='Congresso/Feira')),
                ('motviagemEstudoCursos', models.BooleanField(default=False, verbose_name='Estudo/Cursos')),
                ('motviagemNegocios', models.BooleanField(default=False, verbose_name='Negócios')),
                ('motviagemParentesAmigos', models.BooleanField(default=False, verbose_name='Parentes/Amigos')),
                ('motviagemReligiao', models.BooleanField(default=False, verbose_name='Religião')),
                ('motviagemCompras', models.BooleanField(default=False, verbose_name='Compras')),
                ('motviagemOutros', models.BooleanField(default=False, verbose_name='Outros')),
                ('meiotransporteAviao', models.BooleanField(default=False, verbose_name='Avião')),
                ('meiotransporteCarro', models.BooleanField(default=False, verbose_name='Carro')),
                ('meiotransporteOnibus', models.BooleanField(default=False, verbose_name='Ônibus')),
                ('meiotransporteMoto', models.BooleanField(default=False, verbose_name='Moto')),
                ('meiotransporteNavio', models.BooleanField(default=False, verbose_name='Navio')),
                ('meiotransporteTrem', models.BooleanField(default=False, verbose_name='Trem')),
                ('meiotransporteOutros', models.BooleanField(default=False, verbose_name='Outros')),
                ('empresa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='apartamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, max_length=50, verbose_name='Descrição')),
                ('tipoapart', models.CharField(choices=[('Simples', 'Simples'), ('Stander', 'Stander'), ('Luxo', 'Luxo'), ('Super Luxo', 'Super Luxo'), ('Duplex', 'Duplex'), ('Cobertura', 'Cobertura'), ('Loft', 'Loft'), ('Rústico', 'Rústico')], max_length=50, verbose_name='Tipo')),
                ('ramal', models.CharField(blank=True, max_length=10, verbose_name='Ramal')),
                ('valordiaria', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor da diária')),
                ('observacao', models.CharField(blank=True, max_length=255, verbose_name='Observação')),
                ('tipostatus', models.CharField(choices=[('Livre', 'Livre'), ('Ocupado', 'Ocupado'), ('Reservado', 'Reservado'), ('Em manutenção', 'Em manutenção'), ('Outro', 'Outro')], max_length=50, verbose_name='Tipo')),
                ('empresa', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='home.empresa')),
            ],
        ),
    ]
