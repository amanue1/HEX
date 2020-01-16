from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    FRESHMAN = '1'
    SOPHOMORE = '2'
    JUNIOR = '3'
    SENIOR = '4'
    GC = '5'

    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, '1'),
        (SOPHOMORE, '2'),
        (JUNIOR, '3'),
        (SENIOR, '4'),
        (GC, '5'),
    ]

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]
    

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')
    date_of_birth = models.DateField(default='1998-05-23')
    department = models.CharField(max_length=100)
    year_in_school = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    I_can_program = models.BooleanField(blank=False, null=True)
    why_join_HEX = models.TextField()
