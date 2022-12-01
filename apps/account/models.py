from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from .utils import send_custom_email

__all__ = ['User','OtpCode']

class UserManager(BaseUserManager):
    def create_user(self,phone_number,email,full_name,password):
        if not phone_number:
            raise ValueError('user must have phone number')

        if not email:
            raise ValueError('user must have email number')

        if not full_name:
            raise ValueError('user must have full_name number')

        if not password:
            raise ValueError('user must have password number')


        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,phone_number,email,full_name,password):
        if not phone_number:
            raise ValueError('user must have phone number')

        if not email:
            raise ValueError('user must have email number')

        if not full_name:
            raise ValueError('user must have full_name number')

        if not password:
            raise ValueError('user must have password number')


        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number,
            full_name=full_name,
            is_admin=True,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.CharField(max_length=256,unique=True)
    phone_number = models.CharField(max_length=11,unique=True)
    full_name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email','full_name']

    def __str__(self):
        return self.full_name

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def send_email(self,sunject,message):
        send_custom_email(self.email,sunject,message)

    
class OtpCode(models.Model):
    phone = models.CharField(max_length=11,unique=True)
    code = models.PositiveSmallIntegerField()


    def check_code(self,code):
        if code == self.code:
            return True
        else:
            return False

    def __str__(self):
        return str(self.phone)