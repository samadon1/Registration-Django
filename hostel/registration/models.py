from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Registration(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    CARD = (
        ('G', "Ghana Card"),
        ('N', "National Health_Insurance Card"),
        ('V', "Voter's ID Card"),
        ('S', "Student's ID"),
        ('D', "Driver's License"),
    )
    name = models.CharField(max_length=200, verbose_name="")
    contact = PhoneNumberField(max_length=40, null= True, blank = True, verbose_name="")
    gender =  models.CharField(max_length = 2, choices = GENDER, default='F', verbose_name="")
    id_card =  models.CharField(max_length = 2, choices = CARD, default='G', verbose_name="")
    id_number = models.CharField(max_length=10, verbose_name="")

    def __str__(self):
        return self.name
