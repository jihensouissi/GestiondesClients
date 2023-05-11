from django.db import models

# Create your models here.
class Produit(models.Model):
    nom=models.chartFiels(max_length=200,null=True)
    prix=models.FloatField(null=True)