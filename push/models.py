from django.contrib.auth import get_user_model
from django.db import models


class SubscriptionInfo(models.Model):
    browser = models.CharField(max_length=100)
    endpoint = models.URLField(max_length=255)
    auth = models.CharField(max_length=100)
    p256dh = models.CharField(max_length=100)
