from django.conf import settings
from django.db import models
from  django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.
class profiles(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    email = models.EmailField(null=True,blank=False)
    short_intro = models.CharField(max_length=150,default="my intro",null=True,blank="True")
    bio = models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(default='profile_pic/default.jpg',upload_to='profile_pic')
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    facebook_link = models.CharField(max_length=300,default=" ",null=True,blank="True")
    twitter_link = models.CharField(max_length=300,default=" ",null=True,blank="True")
    linkedin_link = models.CharField(max_length=300,default=" ",null=True,blank="True")

    def __str__(self):
        return self.name


def createProfile(sender,instance,created,**kwargs):
    if created:
        newprofile = profiles.objects.create(
            name = instance.username,
            user = instance,
        )
def createUser(sender,instance,created,**kwargs):
    profile = instance
    suser = profile.user 
    if created == False:
        suser.username = profile.name
        suser.email = profile.email
        suser.save()

post_save.connect(createProfile,sender=User)
post_save.connect(createUser,sender=profiles)