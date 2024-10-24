from django.db import models
from django.utils import timezone

# Create your models here.

class EcomUser(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # Auto fields for timestamps
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, default=timezone.now)

    class Meta:
        db_table = 'ecom_user'
        managed = True