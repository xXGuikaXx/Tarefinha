from django.utils import timezone

def get_idade(data_nascimento):
    dia_nascimento = data_nascimento.day
    mes_nascimento = data_nascimento.month
    ano_nascimento = data_nascimento.year

    decremento = 0

    if mes_nascimento < timezone.now().date().month:
        decremento -= 1

    if mes_nascimento == timezone.now().date().month:
        if dia_nascimento < timezone.now().date().day:
            decremento -= 1

    return timezone.now().date().year - data_nascimento.year + decremento