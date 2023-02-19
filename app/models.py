from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES=(
    ('AndhraPradesh','AndhraPradesh'),
    ('Telgana','Telgana'),
    ('Tamilnadu','Tamilnadu'),
    ('Kerla','Kerla'),
    ('Karnataka','Karnataka'),
    ('Goa','Goa'),
)

CATEGORY_CHOICES = (
    ('PF','Perfumes'),
    ('MB','Mobiles'),
    ('FW','FaceWash'),
    ('FC','FaceCream'),
    ('SP','Soaps'),
    ('LP','Laptops'),
    ('TV','Tvs'),
    ('BS','BodySprays'),
)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    Benfits = models.TextField()
    category = models.CharField(choices = CATEGORY_CHOICES, max_length = 2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.name

