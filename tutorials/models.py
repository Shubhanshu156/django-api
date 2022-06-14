from datetime import date
from unicodedata import category
from django.utils import timezone
from signal import default_int_handler
from django.db import models

import uuid

class response(models.Model):
    username = models.CharField(max_length=50,default="")
    description=models.CharField(max_length=200,default="")
    brand=models.CharField(max_length=200,default="shree cement")
    coordinate1=models.CharField(max_length=200,default="")
    coordinate2=models.CharField(max_length=200,default="")
    object_size_height=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    object_size_width=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    ref_object_size_height=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    ref_object_size_width=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_verify=models.BooleanField(default=False)


# models.py
class Upload(models.Model):
    username = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/')
    description=models.CharField(max_length=200,default="")
    brand=models.CharField(max_length=200,default="shree cement")
    coordinate1=models.CharField(max_length=200,default="")
    coordinate2=models.CharField(max_length=200,default="")
    ref_object_size_height=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    ref_object_size_width=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    is_verify=models.BooleanField(default=False)
    
class Register(models.Model):
    username=models.CharField(max_length=50)
    fullname=models.CharField(max_length=50)
    createddate=models.DateField(auto_now_add=True,blank=True)
    createtime=models.TimeField(auto_now_add=True,blank=True)
    lastdate=models.DateField(auto_now=True,blank=True)
    lasttime=models.TimeField(auto_now=True,blank=True)
    is_active=models.BooleanField(default=True)
    is_approved=models.BooleanField(default=False)
    password=models.CharField(max_length=50)
    cat=(
        ("1","Vendor Staff"),
        ("2","Worker"),
        ("3","Employee"),
        ("4","Admin"),
    )
    category = models.CharField(
        max_length = 20,
        default = 'Vendor Staff'
        )
    reg=(
        ("1","Andhra Pradesh"),
        ("2","Arunachal Pradesh"),
        ("3","Assam"),
        ("4","Bihar"),
        ("5","Chandigarh"),
        ("6","Chhattisgarh"),
        ("7","Dadra and Nagar Haveli"),
        ("8","Daman and Diu"),
        ("9","Delhi"),
        ("10","Goa"),
        ("11","Gujarat"),
        ("12","Haryana"),
        ("13","Himachal Pradesh"),
        ("14","Jammu and Kashmir"),
        ("15","Jharkhand"),
        ("16","Karnataka"),
        ("17","Kerala"),
        ("18","Lakshadweep"),
        ("19","Madhya Pradesh"),
        ("20","Maharashtra"),
        ("21","Manipur"),
        ("22","Meghalaya"),
        ("23","Mizoram"),
        ("24","Nagaland"),
        ("25","Orissa"),
        ("26","Pondicherry"),
        ("27","Punjab"),
        ("28","Rajasthan"),
        ("29","Sikkim"),
        ("30","Tamil Nadu"),
        ("31","Tripura"),
        ("32","Uttaranchal"),
        ("33","Uttar Pradesh"),
        ("34","West Bengal"),

    )
    created_by=models.CharField(max_length=50,default="")
    updated_by=models.CharField(max_length=50,default="")
    region=models.CharField(max_length=50,default="Rajasthan")
    email=models.CharField(max_length=50,default="shubhanshusharma2712@gmail.com")
    phone=models.CharField(max_length=10,default='1234567890')
    ucode=models.CharField(max_length=10)

def nameFile(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


