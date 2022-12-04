from django import template
from apps.home.models import Category

register = template.Library()

@register.inclusion_tag('inc/message.html', takes_context=True)
def messages(context):
    return context

@register.inclusion_tag('inc/navbar.html', takes_context=True)
def navbar(context):
    context['categories'] = Category.objects.all()
    return context