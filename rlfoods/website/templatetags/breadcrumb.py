from django import template

register = template.Library()


@register.inclusion_tag('layouts/breadcrumb.html')
def breadcrumb(*args, **kwargs):
    page_title = "Reliable Foods"
    deep_level1_title = kwargs['deep_level1_title'] if 'deep_level1_title' in kwargs else ''
    deep_level1_link = kwargs['deep_level1_link'] if 'deep_level1_link' in kwargs else ''

    deep_level2_title = kwargs['deep_level2_title'] if 'deep_level2_title' in kwargs else ''
    deep_level2_link = kwargs['deep_level2_link'] if 'deep_level2_link' in kwargs else ''
    page_detail_title = kwargs['page_detail_title'] if 'page_detail_title' in kwargs else ''

    return {
        "page_title" : page_title,
        "deep_level1_title" : deep_level1_title,
        "deep_level1_link" : deep_level1_link,
        "deep_level2_title" : deep_level2_title, 
        "deep_level2_link" : deep_level2_link,
        "page_detail_title" : page_detail_title
    }
