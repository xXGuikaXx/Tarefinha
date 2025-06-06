# Generated by Django 5.2.1 on 2025-05-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do Medico', max_length=200, verbose_name='Nome')),
                ('crm', models.CharField(help_text='CRM do Medico', max_length=6, verbose_name='CRM')),
                ('telefone', models.CharField(help_text='Telefone do Medico', max_length=200, verbose_name='Telefone')),
                ('email', models.CharField(help_text='Email do Medico', max_length=200, verbose_name='Email')),
                ('data_nacimento', models.DateField(help_text='Data de Nacimento', verbose_name='Data de Nacimento')),
                ('cpf', models.CharField(help_text='CPF do Medico', max_length=12, verbose_name='CPF')),
                ('status', models.CharField(help_text='Status do Medico', max_length=100, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Medico',
                'verbose_name_plural': 'Medicos',
            },
        ),
    ]
