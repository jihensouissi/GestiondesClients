from django.db import models

# Create your models here.
class Client(models.Model):
    nom=models.chartFiels(max_length=200,null=True)
    telephone=models.chartFiels(max_length=200,null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)