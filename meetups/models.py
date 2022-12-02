
from django.db import models
from django.contrib.auth.models import AbstractUser




# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    groups=models.CharField(max_length=200, null=True)
    user_permissions=models.CharField(max_length=200, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Location(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    def __str__(self):
       return f'{self.name}-({self.address})'

class Participant(models.Model):
    email=models.EmailField(max_length=254)
    def __str__(self):
        return self.email
    

class Meetup(models.Model):
      organizer_email=models.EmailField(max_length=254, null=True)
      title=models.CharField(max_length=200)
      slug=models.SlugField(unique=True)
      description=models.TextField()
      image=models.ImageField(upload_to='images')
      location=models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
      participant=models.ManyToManyField(Participant, blank=True, null=True)


      def __str__(self):
          return f'{self.title}-({self.slug})'

class About(models.Model):
    description=models.TextField()
    image=models.ImageField(upload_to='about_images')

    def __str__(self):
          return self.description

class Contact(models.Model):
    description=models.TextField()
    image=models.ImageField(upload_to='contact_images')
      
    def __str__(self):
          return self.description 







    