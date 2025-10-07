from django import template
from blog.models import post

register = template.Library()

@register.simple_tag(name='totalpost')
def func():
    posts = post.objects.filter(status=1).count
    return posts

@register.simple_tag(name='posts')
def func1():
    posts = post.objects.filter(status = 1)
    return posts

@register.filter
def snippet(value):
    return value[:255]

@register.inclusion_tag('blog/latestposts.html')
def latestpost():
    posts = post.objects.filter(status = 1).order_by('-published_date')[:4]
    return {'posts':posts}