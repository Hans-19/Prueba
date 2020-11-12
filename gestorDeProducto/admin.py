from django.contrib import admin
from gestorDeProducto.models import Producto
from .import views

class ProductoAdmin(admin.ModelAdmin):
    list_display=('stock','descripcion','precioCosto','precioVenta')
    list_display_links=('stock','descripcion','precioCosto','precioVenta')
    list_filter=('id',)
    search_fields=('stock','precioCosto','precioVenta')

admin.site.register(Producto, ProductoAdmin)