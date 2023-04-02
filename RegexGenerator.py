import random
import string
from PIL import Image, ImageDraw, ImageFont

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

# Função para criar uma imagem de gradiente de botão
def create_button_gradient(size, colors, text_color):
    img = Image.new('RGBA', size, color=colors[0])
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, size[0] // 2, size[1]), fill=colors[0], outline=None)
    draw.rectangle((size[0] // 2, 0, size[0], size[1]), fill=colors[1], outline=None)
    font_size = int(size[1] * 0.6)
    font = ImageFont.truetype('arial.ttf', font_size)
    text_width, text_height = draw.textsize('Ok', font=font)
    draw.text(((size[0] - text_width) // 2, (size[1] - text_height) // 2), 'Ok', fill=text_color, font=font)
    return img.tobytes()
