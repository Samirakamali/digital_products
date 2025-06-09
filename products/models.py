from django.db import models
from django.utils.translation import gettext_lazy as _ 

# Create your models here.
class Category(models.Model):
<<<<<<< HEAD
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE) 
    title = models.CharField(_('title'), max_length=50)  
    description = models.TimeField(_('description'), blank=True)
=======
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)  # baraye subcategory b khodesh foreinkey mizanam. va inke agar category parent hazf shod badesh che etefaqi biofte
    title = models.CharField(_('title'), max_length=50)  # the first arguman is for verbose_name(what I expect be showun as name of product rathe than its saved name in database!)
    description = models.TextField(_('description'), blank=True)
>>>>>>> 6831b5c (models added to admin.)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:  
        db_table = 'categories'  
        verbose_name = _('Category') 
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title 


class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True,upload_to='categories')
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('product'), blank=True, null=True, on_delete=models.CASCADE) 
    title = models.CharField(_('title'), max_length=50)
<<<<<<< HEAD
    description = models.TimeField(_('description'), blank=True)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/')
=======
    description = models.TextField(_('description'), blank=True)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/') #taeen sal mah ruz
>>>>>>> 6831b5c (models added to admin.)
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

