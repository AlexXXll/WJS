from django import template
from cms.models.pagemodel import Page

register = template.Library()

def cms_navigation():
    cms_pages = Page.objects.filter(in_navigation=True, published=True)
    return {'cms_pages': cms_pages}

register.inclusion_tag('GIF.html')(cms_navigation)