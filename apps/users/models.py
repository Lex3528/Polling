from django.contrib.auth.models import AbstractUser, Group, UserManager
from django.db import IntegrityError, models


class User(AbstractUser):
    VISITORS_GROUP_NAME = 'visitors'
    ADMINISTRATORS_GROUP_NAME = 'administrators'

    GROUPS = {
        ADMINISTRATORS_GROUP_NAME: 'Администратор',
        VISITORS_GROUP_NAME: 'Посетители'
    }

    def __str__(self):
        if self.username:
            return self.username
        else:
            return str(self.phone)