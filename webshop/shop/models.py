from django.db import models

class products(models.Model):
    productName = models.CharField(max_length=300)
    productPrice = models.CharField(max_length=20)
    productDescription = models.TextField()
    productImg1 = models.Charfield(max_length=300) 
    productImg2 = models.Charfield(max_length=300) 
    productImg3 = models.Charfield(max_length=300) 