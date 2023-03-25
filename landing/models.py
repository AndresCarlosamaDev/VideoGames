from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=100)
    correo = models.EmailField()
    
    def __str__(self) -> str:
        usuario = 'Usuario: ' + self.nombre
        return usuario

class JuegoPopular(models.Model):
    nombreJuego = models.CharField(max_length=100)
    rating =  models.FloatField()
    tipo = models.CharField(max_length=50)
    descargas = models.FloatField()
    imagen = models.ImageField(upload_to='../landing/static/images', null=True)
    
    def __str__(self) -> str:
        nombreJuego = self.nombreJuego
        return nombreJuego
    
class JuegoJugador(models.Model):
    nombreJuego = models.CharField(max_length=50)
    desarrollador = models.CharField(max_length=50)
    estreno = models.CharField(max_length=50)
    genero = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=50, blank=True, default='No completado')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        formato = self.nombreJuego + ' | ' + self.user.username
        return formato