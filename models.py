from django.conf import settings
from django.db import models
#from django.utils import timezone


from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    id_nomina = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return f"{self.nombre} - {self.id_nomina}"

class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    nombre_video = models.CharField(max_length=50)
    extension_video = models.CharField(max_length=5)
    tamano_video = models.FloatField()

    def __str__(self):
        return f"{self.nombre_video} - {self.extension_video}"

class VideoUsuario(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_usuario.nombre} - {self.id_video.nombre_video}"
