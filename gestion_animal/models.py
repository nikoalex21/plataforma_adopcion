from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    cedula = models.CharField(max_length=20)
    telefono = models.CharField(max_length=15)
   
    ROLES = (
        ('veterinario', 'Centro Veterinario'),
        ('hogar_paso', 'Hogar de Paso '),
        ('adoptante', 'Adoptante'),
        ('colaborador', 'Colaborador'),
        ('ayudador', 'Ayudador'),
    )
    
    rol = models.CharField(max_length=20, choices=ROLES)

    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.rol}"

class Animalito(models.Model):
   
    ESTADOS = (
        ('calle', 'En la calle'),
        ('hogar_paso', 'En hogar de paso'),
        ('revisado_veterinario', 'Revisado por el veterinario'),
        ('adoptado', 'Adoptado'),
    )

    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    edad = models.IntegerField()
    descripcion = models.TextField()
    descripcion_veterinario = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='calle', null=True)  
    ayudador = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='animalitos/', blank=True, null=True)
    hogar = models.ForeignKey(Perfil, on_delete=models.SET_NULL, null=True, blank=True, related_name='animales')

    def __str__(self):
        return self.nombre

class HogarDePaso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    
class SolicitudAdopcion(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    animal = models.ForeignKey(Animalito, on_delete=models.CASCADE)
    adoptante = models.ForeignKey(User, on_delete=models.CASCADE)  
    nombre = models.CharField(max_length=100)  
    edad = models.IntegerField()
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    hogar = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='solicitudes', null=True)

    def __str__(self):
        return f"Solicitud de {self.nombre} para adoptar {self.animal.nombre}"
    

# modulo de ayudas 
class Donacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  
    cantidad = models.DecimalField(max_digits=10, decimal_places=2) 
    fecha = models.DateTimeField(auto_now_add=True)  
    comentario = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"Donación de {self.cantidad} por {self.usuario if self.usuario else 'Anónimo'}"


class Ayuda(models.Model):
    TIPO_AYUDA = [
        ('comunidad', 'Comunidad'),
        ('gobierno', 'Gobierno'),
    ]

    tipo = models.CharField(max_length=50, choices=TIPO_AYUDA)  
    descripcion = models.TextField()  
    fecha = models.DateTimeField(auto_now_add=True)  
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)  
    donacion = models.ForeignKey(Donacion, on_delete=models.CASCADE, related_name="ayudas", null=True, blank=True)

    def __str__(self):
        return f"Ayuda {self.tipo} de {self.cantidad}"

