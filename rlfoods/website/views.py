from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from backend.models import Banner, GridBanner, Product, Notice, Feedbacks, ProductCategory, Blog, About
from django.contrib import messages
from .form import FeedbackForm

def index(request: HttpRequest) -> HttpResponse:
    banner = Banner.objects.filter(publish=True).first()
    products = Product.objects.filter(publish=True).all()
    product_categories = ProductCategory.objects.filter(publish=True).all()
    grid_banners = GridBanner.objects.filter(publish=True).all()[:2]
    latest_blogs = Blog.objects.filter(publish=True).order_by('-id').all()[:3]

    return render(request, template_name='index.html', context={
        'banner': banner,
        'products': products,
        'product_categories': product_categories,
        'latest_blogs': latest_blogs,
        'grid_banners' : grid_banners
    })


def about(request: HttpRequest) -> HttpResponse:
    about = About.objects.first()
    return render(request, template_name='about.html', context={
        'about' : about
    })


def product(request: HttpRequest) -> HttpResponse:
    category = request.GET.get('category')
    products = Product.objects.get_queryset()
    if category:
        products = products.filter(category__slug=category)
    products = products.filter(publish=True).all()
    hot_products = Product.objects.filter(publish=True, product_type='hot').all()
    upcomming_products  = Product.objects.filter(publish=True, product_type='upcomming').all()
    product_categories = ProductCategory.objects.filter(publish=True).all()
    return render(request, template_name='product.html', context={
        'product_categories' : product_categories,
        'products' : products,
        'hot_products' :hot_products,
        'upcomming_products': upcomming_products
    })


def product_detail(request: HttpRequest, slug:str) -> HttpRequest:
    return render(request, template_name='product-details.html')


def blog(request: HttpRequest) -> HttpResponse:
    blogs = Blog.objects.filter(publish=True).order_by('-id').all()
    return render(request, template_name='blog.html', context={'blogs': blogs})


def blog_detail(request: HttpRequest, slug) -> HttpResponse:
    return render(request, template_name='blog-details.html')


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            desc = form.cleaned_data['description']
            feedback = Feedbacks(name=name, email=email, description=desc)
            feedback.save()
            messages.add_message(request, messages.SUCCESS, 'Your feedback has been successfully sent.')
    form = FeedbackForm()
    return render(request, template_name='contact.html', context={'form': form})


def notice(request: HttpRequest) -> HttpResponse:
    notices = Notice.objects.filter(publish=True).order_by('-id').all()
    return render(request, template_name='notice.html', context={'notices': notices})


def notice_detail(request: HttpRequest, slug:str) -> HttpRequest:
    pass


def  error_404(request, exception):
    return render(request, template_name='404.html')