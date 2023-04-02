import random
import string
import re


# Gera uma sequência aleatória de caracteres alfabéticos
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))


# Gera uma expressão regular no formato x|y ou x|y*
def generate_random_regex():
    x = generate_random_string(random.randint(1, 2))
    y = generate_random_string(random.randint(1, 2))
    regex_type = random.randint(1, 2)
    if regex_type == 1:
        regex = f'{x}|{y}'
    else:
        regex = f'{x}|{y}*'

    return regex


def generate_two_regex():
    letras = list(string.ascii_letters)
    regexGerado = []

    while len(regexGerado) != 6:
        regex1 = generate_random_regex()
        regex2 = generate_random_regex()
        regex3 = generate_random_regex()
        regex4 = generate_random_regex()

        for letra in letras:
            x1 = re.fullmatch(regex3, letra) and re.fullmatch(regex1, letra)
            x2 = re.fullmatch(regex3, letra) and re.fullmatch(regex2, letra)
            x3 = re.fullmatch(regex4, letra) and re.fullmatch(regex1, letra)
            x4 = re.fullmatch(regex4, letra) and re.fullmatch(regex2, letra)

            if x3 and x1 and x2 and x4:
                regexGerado.append(regex1)
                regexGerado.append(regex2)
                regexGerado.append(f"resposta 1 = {letra}")
                regexGerado.append(regex3)
                regexGerado.append(regex4)
                regexGerado.append(f"resposta 2 = {letra}")
                break

    return regexGerado