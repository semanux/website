from django.db import models

# Create your models here.

class Subscriber(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=254)
    flag = models.BooleanField(blank=True, default=1)
    
    class Meta:
        ordering = ('created',)