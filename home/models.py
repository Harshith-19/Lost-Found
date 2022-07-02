from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
class LostItem(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)
    image = models.ImageField(null=True, blank=True)
    day_lost = models.DateField(default=date.today)
    lost_by = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)

class FoundItem(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    item_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)
    image = models.ImageField(null=True, blank=True)
    day_found = models.DateField(default=date.today)
    found_by = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.item_name)