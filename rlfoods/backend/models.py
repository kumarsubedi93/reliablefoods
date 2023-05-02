from django.db import models
from django_quill.fields import QuillField
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse

PLACEHOLDER_DIR = f'{settings.STATIC_URL}/placeholder'


class ProductCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', null=False)
    image = models.ImageField(upload_to='product_categories/', null=True, blank=True,
                              help_text='The image size should be 270 * 230 px')
    slug = models.SlugField(max_length=100, null=False, editable=False)
    description = QuillField(null=True, blank=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    @property
    def photo_url(self):
        if self.image:
            return self.image.url
        return f'{PLACEHOLDER_DIR}/placeholder-category.jpg'
    
    @property
    def product_filter_by_category_url(self):
        return reverse('product') + '?category=' + self.slug


class Product(models.Model):

    type_choices = (
        ('normal', 'Normal'),
        ('hot', 'Hot'),
        ('upcomming', 'Upcomming')
    )

    category = models.ForeignKey(ProductCategory, verbose_name='Product Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Product Name')
    slug = models.SlugField(editable=False)
    product_type = models.CharField(max_length=10, choices=type_choices, default='normal')
    short_description = QuillField(verbose_name='Short Description', null=True, blank=True)
    weight = models.CharField(max_length=50, verbose_name='Weight', null=True, blank=True)
    size = models.CharField(max_length=50, verbose_name='Size', null=True, blank=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def product_detail_url(self):
        return reverse('product_detail', args=(self.slug,))
    

    @property
    def photo_url(self):
        photo = self.productimage_set.first()
        if photo:
            return photo.image.url
        return f'{PLACEHOLDER_DIR}/placeholder-product.jpg'
    

    @property
    def category_name(self):
        return self.category.name
    
    @property
    def category_slug(self):
        return self.category.slug
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class About(models.Model):
    content = QuillField(null=False)
    
    def __str__(self) -> str:
        return 'About'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=False, help_text='The image size should be 270 * 270 px')


class Banner(models.Model):
    image = models.ImageField(upload_to='banners/', blank=False)
    link = models.URLField(blank=True)
    short_description = QuillField(verbose_name='Short Description', blank=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.image.url


class GridBanner(models.Model):
    image = models.ImageField(upload_to='grid_banners/', blank=False, help_text='The image size 570 * 270 px')
    link = models.URLField(blank=True, null=True)
    publish = models.BooleanField(default=True)

    @property
    def photo_url(self):
        return  self.image.url

    def __str__(self):
        return ''


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', blank=False)
    slug = models.SlugField(max_length=150, blank=False, editable=False)
    image = models.ImageField(upload_to='blogs/', blank=True, null=True)
    published_date = models.DateTimeField(blank=False, null=False)
    description = QuillField(verbose_name='Description', blank=True, null=True)
    publish = models.BooleanField(default=True)

    @property
    def blog_detail_url(self):
        return reverse('blog_detail', args=(self.slug, ))
    
    @property
    def tgs(self):
        tags = self.blogtag_set.all()
        if tags:
            return ','.join(tag.tag for tag in tags)
        return ''
        

    @property
    def photo_url(self):
        if self.image:
            return self.image.url
        return f'{PLACEHOLDER_DIR}/placeholder-blog.jpg'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class BlogTag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50, verbose_name='Tag')


class Notice(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title', blank=False)
    slug = models.SlugField(max_length=150, blank=False, editable=False)
    published_date = models.DateTimeField(blank=False, null=False)
    description = QuillField(blank=True, null=True)
    image = models.ImageField(upload_to='notices/', blank=True, help_text='The image size should be 600 * 500')
    publish = models.BooleanField(default=True)

    @property
    def photo_url(self):
        if self.image:
            return self.image.url
        return f'{PLACEHOLDER_DIR}/placeholder-notice.jpg'
    
    @property
    def notice_detail_url(self):
        return reverse('notice_detail', args=(self.slug,))

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class SiteInfo(models.Model):
    site_name = models.CharField(max_length=100, blank=False)
    phone_num = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=200, blank=False)
    open_time = models.TimeField(blank=False)
    close_time = models.TimeField(blank=False)
    email = models.EmailField(max_length=200, blank=False)
    google_map_location = models.TextField(blank=True)


class Feedbacks(models.Model):
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Feedbacks'
