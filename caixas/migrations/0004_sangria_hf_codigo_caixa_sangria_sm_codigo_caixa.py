# Generated by Django 4.2.3 on 2023-08-02 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixas', '0003_entrada_de_notas_hf_dataemissão_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sangria_hf',
            name='Codigo_caixa',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='sangria_sm',
            name='Codigo_caixa',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
