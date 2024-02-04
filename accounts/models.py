from django.urls import reverse , reverse_lazy
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Userprofile(models.Model):
    bio = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_picture', default= 'default_profile_picture.png')

    def get_absolute_url(self):
        return reverse("profile", kwargs={"pk" : self.pk})
    


class AddEducation(models.Model):
    school = models.CharField(max_length = 50)
    degree = models.CharField(max_length = 50)
    field_of_study = models.CharField(max_length = 50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(auto_now_add = True)
    current_school = models.BooleanField(default = False)
    descreption = models.TextField()

class Exp(models.Model):
    job = models.CharField(max_length = 50)
    company = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(auto_now_add = True)
    current_job = models.BooleanField(default = False)
    descreption = models.TextField()


@receiver(post_save, sender= User , dispatch_uid = 'create_userprofile')
def create_userprofile(sender, instance, **kwargs):
    if Userprofile.objects.filter(user = instance).count() == 0:
        Userprofile.objects.create(user = instance)
