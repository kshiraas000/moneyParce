from django import template
register = template.Library()

@register.filter
def dict_get(d, key):
    return d.get(key, 0)

@register.filter
def get_total_spent(ids, spending_dict):
    return sum(spending_dict.get(i, 0) for i in ids)