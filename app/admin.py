from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderPlaced)


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode']


