from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse
from user.managers import UserManager
from user.enums import Role


class User(AbstractUser):
    username = models.CharField(max_length=150, null=False, blank=False,default='#')
    email = models.EmailField(_('email address'), unique=True)
    roles = models.PositiveSmallIntegerField(choices=Role.ROLE_CHOICES,default="1")
    first_name = models.CharField(max_length=15,null=True,blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'roles']
    objects = UserManager()

    def get_absolute_url(self):

        if self.roles == Role.WRITER:
            return reverse('detail-writers', kwargs={'pk': self.pk})

        if self.roles == Role.READER:
            return reverse('detail-writers', kwargs={'pk': self.pk})
        
        if self.roles == Role.ADMIN:
            return reverse('detail-writers', kwargs={'pk': self.pk})

    def __str__(self):
        return self.email

    def is_reader(self):
        return bool(self.roles == Role.READER)    

    def is_writer(self):
        return bool(self.roles == Role.WRITER)

    def is_admin(self):
        return bool(self.roles == Role.ADMIN)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        permissions = [
            ("is_reader", "Reader"),
            ("is_writer", "Writer"),
            ("is_admin", "Admin"),
        ]
