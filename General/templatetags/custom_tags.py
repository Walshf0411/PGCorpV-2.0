from django import template

register = template.Library()

def mod(var, arg):
    return int(var) % arg

def subtract(var, arg):
    return int(var) - arg

register.filter('mod', mod)
register.filter('subtract', subtract)