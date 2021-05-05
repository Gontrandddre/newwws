from django.template import Library
import datetime

register = Library()

@register.filter(expects_localtime=True)
def date_format(value):
    return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")