from django.template import Library
import markdown


register = Library()

@register.filter(name='markdown')
def markdown_filter(value):
    return markdown.markdown(
        value,
        extensions=[
            'extra',
            'codehilite'
        ],
        extension_configs={
            'codehilite': [
                ('css_class', 'highlight')
            ]
        },
        markdown_output='html5'
    )