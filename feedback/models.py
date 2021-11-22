from django.db import models


class FeedBack(models.Model):
    username = models.CharField(null=False, max_length=100)
    email = models.EmailField(null=False, max_length=100)
    phone = models.CharField(null=True, max_length=100)
    message = models.CharField(null=False, max_length=1000)

    def __str__(self):
        return self.email
