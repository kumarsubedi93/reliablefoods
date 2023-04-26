from backend.models import SiteInfo, Product


def sitesettings_processor(request):
    site_info = SiteInfo.objects.first()
    products = Product.objects.order_by('-id').all()[:3]
    return {'site_info': site_info, 'latest_products': products}
 