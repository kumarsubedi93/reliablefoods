
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('products/', views.product, name='product'),
    path('product/<str:slug>', views.product_detail, name='product_detail'),
    path('blogs', views.blog, name='blog'),
    path('blogs/<str:slug>', views.blog_detail, name='blog_detail'),
    path('contacts', views.contact, name='contact'),
    path('notices', views.notice, name='notice'),
    path('notices/<str:slug>', views.notice_detail, name='notice_detail')
]