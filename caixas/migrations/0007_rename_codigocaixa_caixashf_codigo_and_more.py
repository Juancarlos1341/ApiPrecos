# Generated by Django 4.2.3 on 2023-08-03 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caixas', '0006_entrada_de_notas_hf_codigo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caixashf',
            old_name='CodigoCaixa',
            new_name='Codigo',
        ),
        migrations.RenameField(
            model_name='caixassm',
            old_name='CodigoCaixa',
            new_name='Codigo',
        ),
    ]