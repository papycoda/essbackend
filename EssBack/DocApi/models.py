from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('standard', 'Standard User'),
        ('administrator', 'Administrator'),
    )

    username = None
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='standard')
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class ESGProject(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='project_logos/', null=True, blank=True)
    start_date = models.DateField()
    owners_name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    users = models.ManyToManyField(CustomUser, related_name='esg_projects', blank=True)
    userstasks = models.ManyToManyField('UserTask', related_name='projects', blank=True) 

    def __str__(self):
        return self.company_name

class UserTask(models.Model):
    project = models.ForeignKey(ESGProject, on_delete=models.CASCADE, related_name='user_tasks')
    responsible_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    schedule = models.DateTimeField()

    def __str__(self):
        return self.task_name

