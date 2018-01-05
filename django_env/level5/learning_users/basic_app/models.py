from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserProfileInfo(models.Model):
    # had to add on_delete as its required in django 2.0
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    
    # additional
    portfolio_site = models.URLField(blank=True)
    
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

    
