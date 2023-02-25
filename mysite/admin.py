from django.contrib import admin
from mysite.forms import CustomerForm
from mysite.models import Customer, Product, OrderProduct


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_family','customer_phone','get_jalali_date_birthday')
    form = CustomerForm
    search_fields = ['customer_name', 'customer_family', 'customer_phone']


admin.site.register(Customer, CustomerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','product_price','image_tag')


admin.site.register(Product, ProductAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('customer','product','tedaad','price','price_all','date_sabt')
    raw_id_fields = ['customer']


admin.site.register(OrderProduct, OrderProductAdmin)

