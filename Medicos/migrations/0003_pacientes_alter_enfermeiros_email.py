# Generated by Django 5.2.1 on 2025-05-21 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0002_enfermeiros_alter_medico_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], help_text='Sexo do Paciente', max_length=100, verbose_name='Sexo')),
                ('rg', models.CharField(help_text='RG do Paciente', max_length=10, verbose_name='RG')),
                ('nome_mae', models.CharField(help_text='Nome da Mãe', max_length=200, verbose_name='Nome Comopleto')),
                ('nome_pai', models.CharField(help_text='Nome do Pai', max_length=200, verbose_name='Nome Colpleto')),
                ('telefone', models.CharField(help_text='Telefone de contato do Paciente', max_length=200, verbose_name='Telefone')),
                ('telefone_segundo', models.CharField(help_text='Segundo Telefone de contato Paciente', max_length=200, verbose_name='Telefone')),
                ('email', models.CharField(help_text='Email do Paciente', max_length=200, verbose_name='Email')),
                ('tipo_sanguineo', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O'), ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], help_text='Tipo de Sanguineo', max_length=100, verbose_name='Tipo de Sanguineo')),
            ],
        ),
        migrations.AlterField(
            model_name='enfermeiros',
            name='email',
            field=models.CharField(help_text='Email do Enfermeiro', max_length=200, verbose_name='Email'),
        ),
    ]
