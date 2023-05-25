from django.db import models
from django.urls import reverse

# Create your models here.

STATUSES = (
    ('Rejected', 'Rejected'),
    ('Under analysis', 'Under analysis'),
    ('Approved', 'Approved'),
)

class Role(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('role_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
    
class Intern(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')

    def get_absolute_url(self):
        return reverse('intern_detail', kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.name
    
class RoleStatus(models.Model):
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.CharField(max_length=14, choices=STATUSES, default='Under analysis')
    def __str__(self):
        return self.role.name + " - " + self.intern.name

