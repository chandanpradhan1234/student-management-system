from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30,null=True)
    email = models.EmailField(max_length=30,null=True)
    city = models.TextField(max_length=30,null=True)
    desc = models.TextField(max_length=30,null=True)
    

    def __str__(self):
        return self.name + " - " + self.email


class Student(models.Model):
    fname = models.CharField(max_length=50,null=True)
    lname = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    # dob = models.DateField(blank=True, null=True)
    # dob = models.DateTimeField(blank=True, null=True)

    boolChoice =(
        ("M","Male") ,("F" , "Female")
    )
    gender = models.CharField(max_length=1, choices=boolChoice, null=True)

    collage = models.CharField(max_length=50,null=True)
    city = models.TextField(max_length=50,null=True)
    course = models.TextField(max_length=50,null=True)
    photo = models.ImageField(upload_to='Student',null=True)
    # photo = models.ImageField(upload_to='images/')
    ano = models.CharField(max_length=50,null=True)
    pno = models.CharField(max_length=50,null=True)
    phno = models.CharField(max_length=50,null=True)

    # placement deatils:
    semester = models.TextField(max_length=50,null=True)
    company = models.TextField(max_length=50,null=True)
    location = models.TextField(max_length=50,null=True)
    package = models.TextField(max_length=50,null=True)
    job = models.TextField(max_length=50,null=True)
    

    # Performance Deatils :
    percent = models.CharField(max_length=50,null=True)
    grade = models.TextField(max_length=50,null=True)
    activity = models.TextField(max_length=40,null=True)

    
    def __str__(self):
        return self.fname + " - " + self.collage + " - " + self.phno + " - " + self.percent


class Faculty(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    # dob = models.DateTimeField(blank=True, null=True)
    # dob = models.DateTimeField(blank=True, null=True)

    boolChoice = (
        ("M", "Male"), ("F", "Female")
    )
    gender = models.CharField(max_length=1, choices=boolChoice, null=True)

    collage = models.CharField(max_length=50, null=True)
    ano = models.CharField(max_length=50, null=True)
    phno = models.CharField(max_length=50, null=True)
    exp = models.CharField(max_length=50, null=True)

    
    def __str__(self):
        return self.name + " - " + self.collage + " - " + self.exp
