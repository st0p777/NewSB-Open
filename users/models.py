from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class Users(AbstractUser):
    USER_STATUS = (
        (1, _('Customer')),
        (2, _('Performer')),
        (3, _('Manager')),
        (4, _('Admin')),
        (5, _('Developer'))
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    status = models.IntegerField(choices=USER_STATUS, default=1)



