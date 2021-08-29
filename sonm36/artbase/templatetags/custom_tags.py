import json
from django import template

register = template.Library()


@register.filter
def jsonify(data):
    if isinstance(data, dict):
        return data
    else:
        return json.loads(data)
