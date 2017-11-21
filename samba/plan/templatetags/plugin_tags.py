from django import template

register = template.Library()


@register.filter
def to_readable_name(plugin_name):
    plugin_name = plugin_name.replace('-', ' ')

    return plugin_name.title()
