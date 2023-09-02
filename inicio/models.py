from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Campera(models.Model):
    talle = models.CharField(max_length=50)
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.talle}"
    
class Chaleco(models.Model):
    talle = models.CharField(max_length=50)
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.talle}"
    
class Pantalon(models.Model):
    talle = models.IntegerField()
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50) 
    
    class Meta:
        verbose_name = "Pantalon"
        verbose_name_plural = "Pantalones"
    
    def __str__(self):
        return f"{self.talle}"
    
class Chaparreras(models.Model):
    talle = models.CharField(max_length=50)
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Chaparreras"
        verbose_name_plural = "Chaparreras"
    
    def __str__(self):
        return f"{self.talle}"
        
class Guantes(models.Model):
    talle = models.CharField(max_length=50)
    color1 = models.CharField(max_length=50)
    color2 = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
        
    class Meta:
        verbose_name = "Guantes"
        verbose_name_plural = "Guantes"
    
    def __str__(self):
        return f"{self.talle}" 
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"     
    
# class Accesorios(models.Model):
  #  muslera    