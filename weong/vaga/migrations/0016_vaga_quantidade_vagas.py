# Generated by Django 5.1.4 on 2025-03-10 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaga', '0015_rename_candidato_candidatura_voluntario'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaga',
            name='quantidade_vagas',
            field=models.IntegerField(default=1, help_text='Quantidade de vagas'),
        ),
    ]
