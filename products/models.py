from django.db import models
from django.utils.translation import gettext_lazy as _  # for supporting persian language or translation from english

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)  # baraye subcategory b khodesh foreinkey mizanam. va inke agar category parent hazf shod badesh che etefaqi biofte
    title = models.CharField(_('title'), max_length=50)  # the first arguman is for verbose_name(what I expect be showun as name of product rathe than its saved name in database!)
    description = models.TimeField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:  # baraye ezafe kardan vizegihaye ezafeh
        db_table = 'categories'  # ino mizara, ta esme jadvalmo tu database khodam malum konam vagarna default esme app_esme model mishe!
        verbose_name = _('Category')  # esme categori k admin mibine
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TimeField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True,upload_to='categories')
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'), blank=True)# many to many yani yeki az productha mitune jozi bishtar az yek categori bashe
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('product'), blank=True, null=True, on_delete=models.CASCADE) # chanta file b yek product vasl bshan. baraye hamin az ravesh forienkey estafade mikonim
    title = models.CharField(_('title'), max_length=50)
    description = models.TimeField(_('description'), blank=True)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/') #taeen sal mah ruz
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

