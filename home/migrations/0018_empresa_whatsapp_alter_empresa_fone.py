# Generated by Django 4.1.7 on 2023-04-11 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_apartamentos_valordiaria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='whatsApp',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='WhatsApp'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='fone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Fone'),
        ),
    ]
