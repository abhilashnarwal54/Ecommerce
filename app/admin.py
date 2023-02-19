from django.contrib import admin
from .models import Product,Customers
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','discounted_price','description','Benfits','category','product_image']


@admin.register(Customers)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','user','locality','city','state','zipcode']