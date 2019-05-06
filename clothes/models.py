from django.db import models
from enum import Enum          

from user.models import User
from user.models import Gender


class Cloth(models.Model):
    item_id     = models.CharField(max_length=200) 
    user_gender = models.CharField(max_length=3, choices = Gender.choices())
    img_ref     = models.CharField(max_length=200)
    page_ref    = models.CharField(max_length=200)
    temp_min    = models.CharField(max_length=20)
    temp_max    = models.CharField(max_length=20)
    hearts      = models.ManyToManyField(User, related_name='hearts')

    @property
    def total_hearts(self):
        return self.hearts.count()

    class Meta:                
        db_table = "clothes"
