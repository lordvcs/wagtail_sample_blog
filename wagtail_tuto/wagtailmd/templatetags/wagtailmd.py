from django.template import Library
import markdown


register = Library()

@register.filter(name='markdown')
def markdown_filter(value):
    return markdown.markdown(
        value,
        markdown_output='html5'
    )