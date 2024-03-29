from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) 
    description = models.TextField(blank = True) 
    price       = models.DecimalField(max_digits = 10000, decimal_places=2) 
    summary     = models.TextField()
    featured    = models.BooleanField(default= False)

    def get_absolute_url(self):
        return reverse("product-detail",kwargs = {"id" : self.id})