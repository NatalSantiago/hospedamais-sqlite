# Generated by Django 4.1.7 on 2023-04-13 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_hospedes_meiotransporteaviao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospedes',
            name='cep',
            field=models.CharField(blank=True, max_length=10, verbose_name='Cep'),
        ),
    ]