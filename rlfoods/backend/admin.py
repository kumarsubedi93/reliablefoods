from django.contrib import admin
from .models import (ProductCategory,
                     Product,
                     ProductImage,
                     Banner,
                     GridBanner,
                     Blog,
                     BlogTag,
                     Notice,
                     SiteInfo,
                     Feedbacks,
                     About
                     )
from django.utils.safestring import mark_safe


class AdminCssMixing:
    class Media:
        css = {
            'all': ('admin/css/cls.css', )
        }


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin, AdminCssMixing):
    list_display = ('name', 'display_image', 'publish')

    @admin.display(description='Image')
    def display_image(self, obj):
        return mark_safe(
            f'<img src="{obj.photo_url}" alt="no alt" width="150" height="100"/>'
        )


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    readonly_fields = ('id', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, AdminCssMixing):
    list_display = ('category', 'name', 'get_image', 'product_type', 'publish')
    inlines = (ProductImageInline, )
    list_filter = ('product_type', )

    @admin.display(description='Image')
    def get_image(self, obj):
        return mark_safe(
            f'<img src="{obj.photo_url}" alt="no alt" width="150" height="100"/>'
        )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin, AdminCssMixing):
    
    def has_add_permission(self, obj) -> bool:
        return False


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin, AdminCssMixing):
    list_display = ('get_banner_image', )

    @admin.display(description='Banner Image')
    def get_banner_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" alt="no alt" width="500" height="250"/>'
        )


@admin.register(GridBanner)
class GridBannerAdmin(admin.ModelAdmin, AdminCssMixing):
    list_display = ('get_grid_banner_image', 'publish')
    fieldsets = [
        ('Attributes', {'fields': ['image', 'link', 'publish']}),
    ]

    @admin.display(description='Grid Banner Image')
    def get_grid_banner_image(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" alt="no alt" width="300" height="200"/>'
        )


class BlogTagInline(admin.TabularInline):
    model = BlogTag
    extra = 1
    readonly_fields = ('id', )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin, AdminCssMixing):
    inlines = (BlogTagInline, )
    list_display = ('title', 'published_date', 'publish')


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin, AdminCssMixing):
    list_display = ('title', 'get_image', 'published_date', 'publish')

    @admin.display(description='Image')
    def get_image(self, obj):
        return mark_safe(
            f'<img src="{obj.photo_url}" alt="no alt" width="300" height="200"/>'
        )


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'phone_num', 'address', 'email')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Feedbacks)
class FeedbackAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    list_display = ('name', 'email', 'description')

