from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Postjob(models.Model):
    Postjob_id=models.AutoField
    Postjob_img=models.ImageField(upload_to="static/images")
    Postjob_name=models.CharField(max_length=100)
    Postjob_dis=models.CharField(max_length=300)
    pub_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=50)
    def __str__(self):
        return self.category
    

    


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    protfolio_site =models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to="static/img-profile", blank=True)
    def __str__(self):
        return self.User.username




