from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator

class User(AbstractUser):
    username = models.CharField(
        max_length = 30,
        unique = True,
        validators = [RegexValidator(
            regex = r'^@\w{3,}$',
            message = 'username must consist of @ followed by atleast 3 alpha numericals'
            )]
    )

    first_name = models.CharField(
        max_length = 50,
        unique = False,
        validators = [RegexValidator(
            regex = r'^[^@#$%^]{2,}$',
            message = 'first name cant contain "@ # $ % ^"'
            )]
    )

    last_name = models.CharField(
        max_length = 50,
        unique = False,
        validators = [RegexValidator(
            regex = r'^[^@#$%^]{2,}$',
            message = 'last name cant contain "@ # $ % ^"'
            )]
    )

    email = models.EmailField(
        unique = True,
        validators = [EmailValidator(
            message = 'email must contain only 1 @ and atleast 1 . and a domain.'
            )]
    )

    bio = models.CharField(
        blank = True,
        max_length = 520,
        unique = False
    )
