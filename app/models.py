from pyexpat import model
from statistics import mode
from tabnanny import verbose
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Client (models.Model) : 
    first_name=models.CharField (max_length=50)
    age = models.BigIntegerField(default=0)

#lzm n7otha gbal product bech enajem en3aytelha fi ligne 37
class Category(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField() 

    class Meta:
        verbose_name_plural="Ctaegories"


    def __str__(self) -> str:
        return f"{self.name}"


class Product(models.Model):
    #au niveau BD Varchar(100) au niveau formulaire input de type text
    name=models.CharField("Nom du produit",max_length=100)
    #au niveau formulaire textarea
    desc=models.TextField()
    #input de type number
    price=models.FloatField(default=0)
    #auto_now_add=date de system w detecti ken saret modification fel date 
    created_at=models.DateField(auto_now_add=True)
    #relation ma bin category w product
    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )

    #bech fi dhash y'affichi nom ta3 produit mch PRODUCT OBJECT 
    def __str__(self) -> str:
        return f"{self.name}"




       
