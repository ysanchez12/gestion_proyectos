import uuid
from django.db import models

# Create your models here.


class Proyecto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Unitario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE, related_name='unitarios')
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    costo = models.FloatField()

    
    def __str__(self):
        return '{} by {}'.format(self.nombre, self.proyecto)