from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class movies(models.Model):
    movies=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pics',default="default.png")
    date=models.DateField()
    duration=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    rating=models.CharField(max_length=50)
    cast=models.TextField(max_length=100)
    trailer=models.CharField(max_length=100)
    price=models.IntegerField(default=0)

class theatre(models.Model):
    theatre = models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    number_of_screens=models.IntegerField()
    

class screen(models.Model):
    screen = models.IntegerField()
    theatre = models.ForeignKey(theatre,on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    no_of_total_seats = models.IntegerField()


class shows(models.Model):
    screen = models.ForeignKey(screen,on_delete=models.CASCADE)
    theatre = models.ForeignKey(theatre ,on_delete= models.CASCADE)
    movies = models.ForeignKey(movies , on_delete= models.CASCADE)
    show_time = models.TimeField()
    show_date = models.DateField()
    no_of_free_seats = models.IntegerField()

class ticket(models.Model):
    shows = models.ForeignKey(shows,on_delete= models.CASCADE)
    name_of_customer = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    no_of_seats = models.IntegerField()

