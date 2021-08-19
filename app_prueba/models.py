from django.db import models
import re
# Create your models here.
# Acá se definen los campos que va a tener mi tabla de la base de datos 
# Se modela la base de datos

class ClienteManager(models.Manager):
    def validador_cliente(self, data): 
        errores = {} # Se crea un diccio de errores 
        if len(data['nombre']) == 0:
            errores['nombre'] = 'Ingrese un nombre'
        if len(data['apellido']) == 0:
            errores['apellido'] = 'Ingrese un apellido'
        if len(data['rut']) == 0:
            errores['rut'] = 'Ingrese un rut'
        if len(data['dv']) == 0:
            errores['dv'] = 'Ingrese un dv'
        if len(data['apellido']) == 0:
            errores['apellido'] = 'Ingrese un apellido'
        #expresiones regulares para validar datos ingresados
        EMAIL = re.compile(
                r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL.match(data['email']):
            errores['email'] = "email invalido"
        return errores

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    creted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClienteManager()