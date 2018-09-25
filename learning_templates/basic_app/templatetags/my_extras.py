from django import template

register = template.library()

@register.filter(name='cut') #decorator

def cut(value,arg):
    """
    This cut out all value of "arg" to string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
