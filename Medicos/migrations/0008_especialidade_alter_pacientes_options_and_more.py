# Generated by Django 5.2.1 on 2025-05-23 10:53

import Medicos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0007_alter_medico_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Ex: Anestesista, Pediatra, ...', max_length=200, verbose_name='Especialidade Medica')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('autualido_em', models.DateTimeField(auto_now=True, verbose_name='Autuado em')),
            ],
            options={
                'verbose_name': 'Especialidade',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.AlterModelOptions(
            name='pacientes',
            options={'verbose_name': ('Paciente',), 'verbose_name_plural': 'Pacientes'},
        ),
        migrations.AlterField(
            model_name='enfermeiros',
            name='coren',
            field=models.CharField(help_text='COREN do enfermeiro', max_length=6, unique=True, verbose_name='COREN'),
        ),
        migrations.AlterField(
            model_name='enfermeiros',
            name='cpf',
            field=models.CharField(help_text='CPF do ENfermeiro', max_length=12, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='enfermeiros',
            name='email',
            field=models.EmailField(help_text='Email do Enfermeiro', max_length=200, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='enfermeiros',
            name='telefone',
            field=models.CharField(help_text='Telefone de Contato', max_length=9, validators=[Medicos.validators.validate_telefone], verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='cpf',
            field=models.CharField(help_text='CPF do Medico', max_length=12, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.CharField(help_text='CRM do Medico', max_length=6, unique=True, verbose_name='CRM'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.EmailField(help_text='Email do Medico', max_length=200, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefone',
            field=models.CharField(help_text='Telefone do Medico', max_length=200, validators=[Medicos.validators.validate_telefone], verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='rg',
            field=models.CharField(help_text='RG do Paciente', max_length=10, unique=True, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='telefone',
            field=models.CharField(help_text='Telefone de contato do Paciente', max_length=200, validators=[Medicos.validators.validate_telefone], verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='telefone_segundo',
            field=models.CharField(help_text='Segundo Telefone de contato Paciente', max_length=200, validators=[Medicos.validators.validate_telefone], verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='tipo_sanguineo',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('Z-', 'O-')], help_text='Tipo de Sanguineo', max_length=100, verbose_name='Tipo de Sanguineo'),
        ),
        migrations.AddField(
            model_name='medico',
            name='especialidade',
            field=models.ManyToManyField(to='Medicos.especialidade'),
        ),
    ]
