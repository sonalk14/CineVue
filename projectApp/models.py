from django.db import models
from django.contrib.auth.models import User

# Create your models here.
type =[("comedy","comedy"),("horror","Horror"),("thriller","Thriller"),("action","Action"),("adventure","Adventure")]
lang = [("hindi","Hindi"),("english","English")]

class Movie(models.Model):
    m_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    desc=models.CharField(max_length=200)
    year = models.IntegerField()
    language =models.CharField(max_length=20,choices=lang)
    category = models.CharField(max_length=20,choices =type)
    image = models.ImageField(upload_to="images")
    video =models.FileField(upload_to="video")
    time=models.CharField(max_length=30)
    cast=models.CharField(max_length=150)

class Wishlist(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="",blank=True,null=True)

class Subscriptions(models.Model):
    s_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    price =models.IntegerField()
    quality = models.CharField(max_length=20)
    resolution=models.CharField(max_length=20)
    

class Suborder(models.Model):
    order_id=models.CharField(max_length=50,default="0")
    subo = models.ForeignKey(Subscriptions,on_delete =models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default="",blank=True,null=True)
    is_completed = models.BooleanField(default=False)


