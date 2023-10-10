from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     TYPES = (
#         ('C', 'School'),
#         ('S', 'Student'),
#         ('SU',"Superuser")
#     )
#     name=models.CharField(max_length=25)
#     username=models.CharField(max_length=35,unique=True,null=False)
#     email=models.EmailField(unique=True)
#     city=models.CharField(max_length=30)
#     pin_code=models.IntegerField(null=True)
#     user_type=models.CharField(choices=TYPES, max_length=5,default='S')

#     def create_user(self, username, email, password, **extra_fields):
#         user = super().create_user(username, email, password, **extra_fields)
#         user.is_superuser = False
#         user.is_staff = False
#         user.save()
#         return user

#     def create_superuser(self, username, email, password, **extra_fields):
#         user = super().create_superuser(username, email, password, **extra_fields)
#         user.user_type = 'SU'
#         user.save()
#         return user
#     # USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS = ['username', 'email']

class User(AbstractUser):
    TYPES = (
        ('S', 'Student'),
        ('SU', 'Superuser'),
        ('SCH', 'School'),
    )
    user_type = models.CharField(choices=TYPES, max_length=5, default='S')

class School(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pin_code = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    grade = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)