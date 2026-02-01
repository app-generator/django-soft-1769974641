# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Articulo(models.Model):

    #__Articulo_FIELDS__
    tipo = models.CharField(max_length=255, null=True, blank=True)
    categoria = models.CharField(max_length=255, null=True, blank=True)
    marca = models.CharField(max_length=255, null=True, blank=True)
    modelo = models.CharField(max_length=255, null=True, blank=True)
    activo = models.BooleanField()

    #__Articulo_FIELDS__END

    class Meta:
        verbose_name        = _("Articulo")
        verbose_name_plural = _("Articulo")


class Entidad(models.Model):

    #__Entidad_FIELDS__
    categoria = models.CharField(max_length=255, null=True, blank=True)
    id_interno = models.CharField(max_length=255, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=True, blank=True)
    ubicacion = models.CharField(max_length=255, null=True, blank=True)
    activo = models.BooleanField()

    #__Entidad_FIELDS__END

    class Meta:
        verbose_name        = _("Entidad")
        verbose_name_plural = _("Entidad")


class Transferencia(models.Model):

    #__Transferencia_FIELDS__
    casootrs = models.CharField(max_length=255, null=True, blank=True)
    persona_recibe = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

    #__Transferencia_FIELDS__END

    class Meta:
        verbose_name        = _("Transferencia")
        verbose_name_plural = _("Transferencia")



#__MODELS__END
