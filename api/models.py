
from django.db import models
class Genero(models.Model):
    genero_id = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=255)

    class Meta:
        db_table = 'Generos'  # Nombre de la tabla en la base de datos


class Usuarios(models.Model):
    usuario_id = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=255)
    fk_genero = models.ForeignKey(Genero, on_delete= models.CASCADE, default=0)
    # Añade más campos aquí si es necesario

    class Meta:
        db_table = 'Usuarios'  # Nombre de la tabla en la base de datos
