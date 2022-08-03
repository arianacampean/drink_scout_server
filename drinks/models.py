from django.db import models


class Drinks(models.Model):
    nume=models.CharField(max_length=50, blank=False, default='')
    modPreparare=models.CharField(max_length=50, blank=False, default='')
    categorie=models.CharField(max_length=300, blank=False, default='')

class Recipes(models.Model):
    idBautura=models.ForeignKey(Drinks, on_delete=models.CASCADE)
    ingredient=models.CharField(max_length=50, blank=False, default='')
    cantitate= models.IntegerField(blank=False,default=0)
    unitateDeMasura=models.CharField(max_length=50, blank=False, default='')
