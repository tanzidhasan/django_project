from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    rollno = models.IntegerField()
    bloodgroup = models.CharField(max_length=10)
    lastblooddonationdate = models.DateField()
    phonenumber = models.BigIntegerField()
    currentlocation = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    posttitle = models.CharField(max_length=150, default='Blood Request post')
    bloodgroup = models.CharField(max_length=10)
    howmanybagsofblood = models.IntegerField()
    patientdisease = models.CharField(max_length=200, default='Patient Diease')
    admittedhospitalname = models.CharField(max_length=75)
    deadlinedate = models.DateField()
    deadlinetime = models.TimeField()
    currentlocation = models.CharField(max_length=50)
    phonenumber = models.BigIntegerField()
    relationwithruetians = models.CharField(max_length=50)
    posteddatetime = models.DateTimeField(default=timezone.now()+timedelta(hours=6))

    def __str__(self):
        return f'{self.posttitle}'

    def get_absolute_url(self):
        return reverse("user-blood_request", kwargs={"pk": self.pk})
    
    