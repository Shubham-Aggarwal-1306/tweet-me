from django.db import models
from django.db.models.signals import post_save

# Create your models here.
from django.conf import settings


User = settings.AUTH_USER_MODEL

class FollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True, through=FollowerRelation)
    

def user_did_save(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    
post_save.connect(user_did_save, sender=User)

# after creating the Profile model, we need to create a signal to create a profile for each user that is created
# we do this by creating a function that listens for the post_save signal from the User model
# the function will create a profile for each user that is created

