from django.template import Library
import datetime

register = Library()


@register.filter(expects_localtime=True)
def date_format(value):

    try:
        format = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        try:
            format = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S+00:00")
        except ValueError:
            format = None

    return format
