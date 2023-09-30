from django import template
 
register = template.Library() # регистрируем наши фильтры

@register.filter(name='censor')
def censor(value, arg):
    censorList = ['жопа', 'срака', 'сраный', 'бля', 'говно', 'сука', ]
    vEdit = value
    result = ''

    for word in censorList:
        vTemp = vEdit.lower().replace(word, arg * len(word))
        vEdit = vTemp

    for i in range(0, len(value)):
        if (value[i] != vEdit[i]):
            result += vEdit[i].upper()
        else:
            result += vEdit[i]

    return result


@register.filter(name='is_filters_uses')
def is_filters_uses(value):
    filters_arg = value.find('&')
    if filters_arg != -1:
        is_first_list_now = value.find('?')
        if value[(is_first_list_now + 1): (is_first_list_now + 5)] == 'page':
            return value[filters_arg:]
        else:
            return ('&' + value[is_first_list_now + 1:])
    else:
        return ''
    