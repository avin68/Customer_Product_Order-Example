from django.db import models
from django.utils.safestring import mark_safe
from jalali_date import date2jalali, datetime2jalali


# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=20, verbose_name='نام مشتری')
    customer_family = models.CharField(max_length=30, verbose_name='نام خانوادگی مشتری')
    customer_phone = models.CharField(max_length=11, verbose_name='شماره تماس مشتری')
    customer_birthday = models.DateTimeField(verbose_name='تاریخ تولد مشتری')

    def __str__(self):
        return self.customer_name + ' ' + self.customer_family

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
        db_table = 'customer'

    def get_jalali_date_birthday(self):
        return date2jalali(self.customer_birthday)

    get_jalali_date_birthday.short_description = 'تاریخ تولد'


class Product(models.Model):
    product_name = models.CharField(max_length=15, verbose_name='نام محصول')
    product_price = models.IntegerField(verbose_name='قیمت محصول')
    product_image = models.ImageField(upload_to='product_img', null=True, blank=True, verbose_name='عکس_محصول')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        db_table = 'product'

    def __str__(self):
        return self.product_name

    def image_tag(self):
        return mark_safe('<img src="%s" width="50"  />' % self.product_image.url)

    image_tag.short_description = 'عکس محصول'


class OrderProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='مشتری')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='کالا')
    tedaad = models.IntegerField(verbose_name='تعداد')
    price = models.IntegerField(verbose_name='قیمت')
    price_all = models.IntegerField(verbose_name='قیمت کل')
    date_sabt = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'
        db_table = 'order'

    def __str__(self):
        return self.customer.customer_name+' '+self.customer.customer_family+'---'+self.product.product_name



