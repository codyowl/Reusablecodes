from django import template

register = template.Library()

@register.simple_tag
def your_tag_name(args):
	return things_you_want
