from django.db import models

class Dress(models.Model):
    color = models.CharField(max_length=50)
    brand = models.CharField(max_length=100)
    styles = models.TextField()
    size = models.CharField(max_length=20)
    imageURL = models.TextField()
    image2URL = models.TextField()
    image3URL = models.TextField()