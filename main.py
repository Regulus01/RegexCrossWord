import re
import PySimpleGUI as sg
import RegexGenerator as rg

# Define o layout da janela
randomRegex = []
for k in range(0, 4):
    randomRegex.append(rg.generate_random_regex())

r1 = randomRegex[0]
r2 = randomRegex[1]
r3 = randomRegex[2]
r4 = randomRegex[3]

# Define o layout do formulário
layout = [
    [sg.Text('Regex crossword 2x2', font=('Helvetica', 18), justification='center', size=(30,1))],
    [sg.Text('  ', size=(3, 1)), sg.Text(r1, size=(3, 1), font=('Helvetica', 16)), sg.Text(r2, size=(12, 1), font=('Helvetica', 16))],
    [sg.Text(r3, font=('Helvetica', 16)), sg.Input(size=(4, 1), key='B1', font=('Helvetica', 16)), sg.Input(size=(4, 1), key='B2', font=('Helvetica', 16))],
    [sg.Text(r4, font=('Helvetica', 16)), sg.Input(size=(4, 1), key='B3', font=('Helvetica', 16)), sg.Input(size=(4, 1), key='B4', font=('Helvetica', 16))],
    [sg.Button('Ok', font=('Helvetica', 16), size=(4, 1), button_color=('white', '#007f5f'))]
]


# Cria a janela com o layout definido
window = sg.Window('Jogo da matriz 2x2', layout, size=(700, 700))

# contador de acertos
contador = 0

# Gera matriz 2x2
matriz = [[' ' for _ in range(2)] for _ in range(2)]

regexLinha = [r1, r2]
regexColuna = [r3, r4]

letrasDigitasB1 = []
letrasDigitasB2 = []
letrasDigitasB3 = []
letrasDigitasB4 = []

while True:
    # Lê os valores da interface
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    letra = ""
    linha = 0
    coluna = 0
    if values['B1'].strip() != "" and values['B1'] not in letrasDigitasB1:
        linha = 0
        coluna = 0
        letra = values['B1'].strip()
        letrasDigitasB1.append(values['B1'].lower())

    if values['B2'].strip() != "" and values['B2'].lower() not in letrasDigitasB2:
        linha = 0
        coluna = 1
        letra = values['B2'].strip()
        letrasDigitasB2.append(values['B2'].lower())

    if values['B3'].strip() != "" and values['B3'].lower() not in letrasDigitasB3:
        linha = 1
        coluna = 0
        letra = values['B3'].strip()
        letrasDigitasB3.append(values['B3'].lower())

    if values['B4'].lower() != "" and values['B4'].lower() not in letrasDigitasB4:
        linha = 1
        coluna = 1
        letra = values['B4'].lower()
        letrasDigitasB4.append(values['B4'].lower())

    matriz[linha][coluna] = letra

    regex1 = regexLinha[linha].strip()
    regex2 = regexColuna[coluna].strip()

    # Verifica se a letra inserida é válida
    if re.fullmatch(regex1, letra) and re.fullmatch(regex2, letra):
        sg.popup('Letra válida!')
        contador += 1
    else:
        sg.popup('Letra inválida!')

    # Se o usuário acertar 4 letras válidas, exibe uma mensagem de vitória
    if contador == 4:
        sg.popup('Você venceu!')
        break

    # Atualiza a interface com a matriz atualizada
    window['B1'].update(matriz[0][0])
    window['B2'].update(matriz[0][1])
    window['B3'].update(matriz[1][0])
    window['B4'].update(matriz[1][1])

# Fecha a janela ao finalizar o jogo
window.close()
