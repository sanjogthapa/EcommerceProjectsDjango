from django.db import models
from django.contrib.auth.models import User


# Create your models here.
PROVINCE_CHOICES = (
    ('province1', 'province1'),
    ('province2', 'province2'),
    ('province3', 'province3'),
    ('province4', 'province4'),
    ('province5', 'province5'),
    ('province6', 'province6'),
    ('province7', 'province7')
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    province = models.CharField(choices=PROVINCE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICE = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    product_image = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.id)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='Pending')

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price




