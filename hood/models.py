from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    health_phone = models.IntegerField(null=True, blank=True)
    police_phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.neighborhood_name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id = neighborhood_id)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=60, blank=True)
    bio = models.TextField(max_length=255, blank=True, default='My bio')
    profile_picture = models.ImageField(upload_to = 'images/', default = 'default.png')
    email = models.CharField(max_length=60)
    location = models.CharField(max_length=50, blank=True, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Business(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    business_name = models.CharField(max_length=100)
    business_email = models.CharField(max_length=60)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='business')

    def __str__(self):
        return f'{self.business_name} Business'

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, business_name):
        return cls.objects.filter(business_name__icontains=business_name).all()


class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='hood_post')
    