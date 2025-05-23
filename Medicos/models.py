from django.core.exceptions import ValidationError
from pydoc import Helper
from django.utils import timezone
from .validators import validate_telefone


from django.db import models


class Especialidade(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name='Especialidade Medica',
        help_text='Ex: Anestesista, Pediatra, ...',
    )

    criado_em = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em',
    )

    autualido_em = models.DateTimeField(
        auto_now=True,
        verbose_name='Autuado em',
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidades'

class Medico(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name='Nome',
        help_text='Nome do Medico'
    )

    especialidade = models.ManyToManyField(Especialidade)

    crm = models.CharField(
        max_length=6,
        verbose_name='CRM',
        help_text='CRM do Medico',
        unique=True
    )
    telefone = models.CharField(
        max_length=200,
        verbose_name='Telefone',
        help_text='Telefone do Medico',
        validators=[validate_telefone]
    )
    email = models.EmailField(
        max_length=200,
        verbose_name='Email',
        help_text='Email do Medico'
    )
    data_nacimento = models.DateField(
        verbose_name='Data de Nacimento',
        help_text='Data de Nacimento'
    )
    cpf = models.CharField(
        max_length=12,
        verbose_name='CPF',
        help_text='CPF do Medico',
        unique=True
    )
    status = models.CharField(
        max_length=100,
        choices= [
            ('Ativo','Ativo'),
            ('Inativo','Inativo')
]
    )



    def clean(self):

        super().clean()
        if (timezone.now().date().year - self.data_nacimento.year) < 18:
            raise ValidationError(f'Você é muito novo para ser médico')

        if len(self.nome) < 3:
            raise ValidationError(f'O nome deve pelo menos 3 digitos')

        idade = get_idade(self.data_nascimento)

        if len(self.crm) < 6:
            raise ValidationError(f'O CRM deve ter 6 digitos')

        if str.isalpha(self.cpf):
            raise ValidationError(f'O cpf não pode conter letras')



    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'

class Enfermeiros(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name='Nome',
        help_text='Nome do Enfermeiro'
    )
    coren = models.CharField(
        max_length=6,
        verbose_name='COREN',
        help_text='COREN do enfermeiro',
        unique=True
    )
    atuacao = models.CharField(
        max_length=200,
        verbose_name='Setor de Atuação',
        help_text='Setor de Atuação do Enfermeiro',
        choices=[
            ('Pediatra','Pediatra'),
            ('Oftamologista','Oftamologista')
        ],
        null=True
    )
    telefone = models.CharField(
        max_length=9,
        verbose_name='Telefone',
        help_text='Telefone de Contato',
        validators=[validate_telefone]
    )
    email = models.EmailField(
        max_length=200,
        verbose_name='Email',
        help_text='Email do Enfermeiro'
    )
    data_nacimento = models.DateField(
        verbose_name='Data de Nacimento',
        help_text='Data de Nacimento'
    )
    cpf = models.CharField(
        max_length=12,
        verbose_name='CPF',
        help_text='CPF do ENfermeiro',
        unique=True
    )
    turno = models.CharField(
        max_length=100,
        choices= [
            ('Manhá','Manhá'),
            ('Tarde','Tarde'),
            ('Noite','Noite'),
            ('Integral','Integral')
],
        verbose_name='Turno',
        help_text='Turno do medico'
    ),
    status = models.CharField(
        max_length=100,
        choices=[
            ('Ativo', 'Ativo'),
            ('Inativo', 'Inativo')
],
        verbose_name='Status',
        help_text='Status do medico'
    )


    def clean(self):
        super().clean()

        if (timezone.now().date().year - self.data_nacimento.year) < 18:
            raise ValidationError(f'Você é muito novo para ser enfermeiro')

        if len(self.nome) < 3:
            raise ValidationError(f'O nome deve pelo menos 3 digitos')

        if len(self.coren) < 6:
            raise ValidationError(f'O CRM deve ter 6 digitos')

        if str.isalpha(self.cpf):
            raise ValidationError(f'O cpf não pode conter letras')


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name='Enfermeiro',
        verbose_name_plural='Enfermeiros'

class Pacientes(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name='Nome',
        help_text='Nome do Paciente',
        null=True
    )
    data_nacimento = models.DateField(
        verbose_name='Data de Nacimento',
        help_text='Data de Nacimento',
        null=True
    )
    sexo = models.CharField(
        max_length=100,
        choices = [
            ('M', 'Masculino'),
            ('F', 'Femenino')
        ],
        verbose_name='Sexo',
        help_text='Sexo do Paciente'
    )
    cpf = models.CharField(
        max_length=12,
        verbose_name='CPF',
        help_text='CPF do Paciente',
        unique=True
    ),
    rg = models.CharField(
        max_length=10,
        verbose_name='RG',
        help_text='RG do Paciente',
        unique=True
    )
    nome_mae = models.CharField(
        max_length=200,
        verbose_name='Nome Comopleto',
        help_text='Nome da Mãe'
    )
    nome_pai = models.CharField(
        max_length=200,
        verbose_name='Nome Colpleto',
        help_text='Nome do Pai'
    )
    telefone = models.CharField(
        max_length=200,
        verbose_name='Telefone',
        help_text='Telefone de contato do Paciente',
        validators=[validate_telefone]
    )
    telefone_segundo = models.CharField(
        max_length=200,
        verbose_name='Telefone',
        help_text='Segundo Telefone de contato Paciente',
        validators=[validate_telefone]
    )
    email = models.CharField(
        max_length=200,
        verbose_name='Email',
        help_text='Email do Paciente'
    )
    tipo_sanguineo = models.CharField(
        max_length=100,
        verbose_name='Tipo de Sanguineo',
        help_text='Tipo de Sanguineo',
        choices = [
            ('A', 'A'),
            ('B', 'B'),
            ('AB','AB'),
            ('O', 'O'),
            ('A+', 'A+'),
            ('B+', 'B+'),
            ('AB+', 'AB+'),
            ('O+', 'O+'),
            ('A-','A-'),
            ('B-','B-'),
            ('AB-','AB-'),
            ('Z-','O-'),
        ]
    )

    def clean(self):
        super().clean()

        if len(self.nome) < 3:
            raise ValidationError(f'O nome deve pelo menos 3 digitos')

        if str.isalpha(self.cpf):
            raise ValidationError(f'O cpf não pode conter letras')


    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Paciente',
        verbose_name_plural = 'Pacientes'


