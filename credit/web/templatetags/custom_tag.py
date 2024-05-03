from django import template

register = template.Library()

@register.filter
def text_slice(text):
	if len(text) > 10:
		text = text[:10] + '..'
		return text
	else :
		return text
