from django.conf import settings
from django.db import models
from django.db.models.deletion import CASCADE


class BaseModel(models.Model):
    creacion_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='creacion_user', null=True, blank=True)


    class Meta:
        abstract = True
