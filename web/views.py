# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Categoria, Producto, Testimonial
# Create your views here.

def index(request):
	mensaje = 'INDEX'
	testimonios = Testimonial.objects.filter(activo=True)
	productos = Producto.objects.filter(activo=True)
	ofertas = Producto.objects.filter(activo=True, oferta=True)
	categorias = Categoria.objects.all()


	context = {'mensaje': mensaje, 'testimonios': testimonios, 'productos': productos, 'ofertas': ofertas, 'categorias': categorias}
	return render(request, 'index.html', context)