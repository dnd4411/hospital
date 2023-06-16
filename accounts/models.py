from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    PROFILE_CHOICES = (
        ('P', 'Patient'),
        ('D', 'Doctor'),
    )

    profile_type = models.CharField(max_length=1, choices=PROFILE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    address_line1 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)

    groups = models.ManyToManyField(Group, blank=True, related_name='user_accounts')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_accounts')

    def __str__(self):
        return self.username
