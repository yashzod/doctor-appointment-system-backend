from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class doctor(models.Model):
    name = models.CharField(max_length=50)
    speciality = models.CharField(max_length=50)

class slot(models.Model):
    doctor = models.ForeignKey(doctor,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available = models.BooleanField()

class patient(models.Model):
    name = models.CharField(max_length=50)

class Appointment(models.Model):
    # doc = models.ForeignKey(doctor,on_delete=models.CASCADE)
    slot = models.ForeignKey(slot,on_delete=models.CASCADE)
    pat = models.ForeignKey(User,on_delete=models.CASCADE)
    # status = models.CharField(max_length=1)