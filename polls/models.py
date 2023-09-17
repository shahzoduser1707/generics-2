from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Workers(models.Model):
    worker_name = models.CharField(max_length=200,default='')
    worker_birthday = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    class Meta:
        db_table = 'Workers'
    def __str__(self) -> str:
        return self.worker_name
    
class Orders(models.Model):
    order_name = models.CharField(max_length=200,default='')
    order_date = models.DateTimeField(default=datetime.now)
    class Meta:
        db_table = 'Orders'
    def __str__(self) -> str:
        return self.order_name
