from django.core.exceptions import ValidationError

def validate_telefone(telefone):
    ddds = [
        11, 12, 13, 14, 15, 16, 17, 18, 19,  # SP
        21, 22, 24,  # RJ
        31, 32, 33, 34, 35, 37, 38,  # MG
        27, 28,  # ES
        41, 42, 43, 44, 45, 46,  # PR
        47, 48, 49,  # SC
        51, 53, 54, 55,  # RS
        61,  # DF
        62, 64,  # GO
        65, 66,  # MT
        67,  # MS
        68,  # AC
        69,  # RO
        71, 73, 74, 75, 77,  # BA
        79,  # SE
        81, 87,  # PE
        82,  # AL
        83,  # PB
        84,  # RN
        85, 88,  # CE
        86, 89,  # PI
        91, 93, 94,  # PA
        92, 97,  # AM
        95,  # RR
        96,  # AP
        98, 99,  # MA
        63  # TO
    ]

    if int(telefone[:2]) not in ddds:
        raise ValidationError(f'DDD invalido')

def validate_cpf(cpf):
    if str(cpf).isalpha():
        return ValidationError(f'O cpf não pode conter letras')

