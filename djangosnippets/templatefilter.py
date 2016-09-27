from django import template

register = template.Library()

@register.filter(name="your_filter_name")
def your_filter_name(args):
	args = args * args
	return args


