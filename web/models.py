# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categoria(models.Model):
	nombre = models.CharField('Nombre', max_length=100)
	descripcion = models.TextField('Descripcion', null=True, blank=True)
	activo = models.BooleanField('Activo', default=True)

	# def es_activo(self):
	# 	if self.activo:
	# 		return ''
	# 	else:
	# 		return 'no-mostrar'

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Categorias"

class Producto(models.Model):
	nombre = models.CharField('Nombre', max_length=100)
	descripcion = models.TextField('Descripcion', null=True, blank=True)
	categoria = models.ForeignKey(Categoria)
	precio = models.CharField('Precio', max_length=10, null=True, blank=True)
	imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
	oferta = models.BooleanField('Oferta', default=False)
	activo = models.BooleanField('Activo', default=True)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Productos"

class Testimonial(models.Model):
	nombre = models.CharField('Nombre del cliente', max_length=100)
	mascota = models.CharField('Nombre de su mascota', max_length=100)
	testimonio = models.CharField('Testimonio', max_length=200)
	activo = models.BooleanField('Activo', default=True)

	# def es_activo(self):
	# 	if self.activo:
	# 		return ''
	# 	else:
	# 		return 'no-mostrar'
	
	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Testimoniales"