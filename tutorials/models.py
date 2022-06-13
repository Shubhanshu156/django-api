from django.db import models



class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)
# models.py
class Hotel(models.Model):
	name = models.CharField(max_length=50)
	hotel_Main_Img = models.ImageField(upload_to='media/')
    
class Register(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="shubhanshusharma2712@gmail.com")
    phone=models.CharField(max_length=10,default='1234567890')
    ucode=models.CharField(max_length=10,default='0')

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


