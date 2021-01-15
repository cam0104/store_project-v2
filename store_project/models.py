from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class BaseModel(models.Model):
    creacion_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='creacion_user', null=True, blank=True)
    fecha_creacion = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    actualizacion_usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='actualizacion_usuario', null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True
