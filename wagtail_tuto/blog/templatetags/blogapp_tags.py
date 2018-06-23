from django.template import Library, loader
# from django.core.urlresolvers import 

register = Library()

@register.simple_tag()
def post_date_url(post, blog_page):
    post_date = post.date
    url = blog_page.url + blog_page.reverse_subpage(
        'post_by_date_slug',
        args=(
            post_date.year,
            '{0:02}'.format(post_date.month),
            '{0:02}'.format(post_date.day),
            post.slug
        )
    )
    return url

@register.inclusion_tag('blog/components/categories_list.html', takes_context=True)
def categories_list(context):
    blog_page = context['blog_page']
    page = context['page']
    categories = page.categories.all
    return {
        'blog_page': blog_page,
        'categories': categories,
        'request': context['request']
    }

@register.inclusion_tag('blog/components/tags_list.html', takes_context=True)
def tags_list(context):
    page = context['page']
    request = context['request']
    blog_page = context['blog_page']
    tags = page.tags.all
    return {
        'tags': tags,
        'request': request,
        'blog_page': blog_page
    }