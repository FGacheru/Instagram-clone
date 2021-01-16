from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length =30)
    image = CloudinaryField('image')
    posted_date= models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length =200)
    