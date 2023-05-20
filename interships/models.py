from django.db import models

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Intern(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='avatars/default.jpg')
    roles = models.ManyToManyField(Role)
    status = models.CharField(max_length=20, default='Under analysis')
    def __str__(self):
        return self.name
