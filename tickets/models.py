from uuid import uuid4
from django.utils.translation import ugettext_lazy as _
from django.db import models
from users.models import Users


class Status(models.Model):
    status = models.CharField(null=False, unique=True, max_length=100)

    class Meta:
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status


class Ticket(models.Model):
    LANGUAGE_CHOICES = (
        ('English', _('English')),
        ('Russian', _('Russian')),
    )
    STATUS_CHOICES = (
        ('Open', _('Open')),
        ('Resolved', _('Resolved')),
        ('Closed', _('Closed')),
        ('Duplicate', _('Duplicate')))
    PRIORITY_CHOICES = (
        ('Critical', _('Critical')),
        ('High', _('High')),
        ('Normal', _('Normal')),
        ('Low', _('Low')),
        ('Very Low', _('Very Low')))
    CHOICES = (
        (0, 'Normal'),
        (1, 'As soon as possible')
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company_name = models.CharField(null=False, max_length=256)
    email = models.EmailField(null=False)
    phone_number = models.CharField(blank=True, max_length=100)
    deadline = models.CharField(null=False, max_length=100)
    if_fast = models.BooleanField(choices=CHOICES, blank=True, default=0, null=True)
    task_priority = models.CharField(choices=PRIORITY_CHOICES, blank=True, default='Normal', max_length=100)
    ticket_status = models.CharField(choices=STATUS_CHOICES, max_length=100, default='Open')
    short_description = models.CharField(null=False, max_length=1000)
    long_description = models.CharField(null=False, max_length=1000)
    market_geography = models.CharField(null=False, max_length=100)
    language_choices = models.CharField(choices=LANGUAGE_CHOICES, max_length=100)
    comments = models.CharField(blank=True, max_length=1000)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_name
