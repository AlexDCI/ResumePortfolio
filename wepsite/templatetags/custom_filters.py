from django import template

register = template.Library()

languege_colors = {

    'python': 'green',
    'java': 'blue',
    'javascript': 'yellow',
    'ruby': 'red',
    'c++': 'purpure'

}

@register.filter(name='colorize_languege')
def colorize_languege(value):
    programing_languege = value.lower()

    color = languege_colors.get(programing_languege, 'black')
    colorize_languege = f'<span style="color : {color}">{value}</span>'
    return colorize_languege
