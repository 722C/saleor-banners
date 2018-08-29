from django import template

from ..models import SaleorBanner

register = template.Library()


@register.inclusion_tag('saleor_banners/dashboard/side_nav_inclusion.html',
                        takes_context=True)
def saleor_banners_side_nav(context):
    return context


@register.inclusion_tag('saleor_banners/banner.html')
def saleor_banner_display(name):
    banner = SaleorBanner.objects.filter(name=name).first()
    return {
        'banner': banner
    }
