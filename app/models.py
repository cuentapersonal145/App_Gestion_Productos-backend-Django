from django.db import models

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_barras = models.CharField(max_length=64, null=False, blank=False)
    descripcion = models.CharField(max_length=255, null=False, blank=False)
    precio_compra = models.PositiveIntegerField()
    precio_venta = models.PositiveIntegerField()
    existencia = models.PositiveIntegerField()
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['descripcion']
        verbose_name = ("Articulo")
        verbose_name_plural = ("Articulos")
        db_table = 'ARTICULO'
        
    def __str__(self):
        return self.descripcion + ' : $' + str(self.precio_venta) + '. [CD:' + self.codigo_barras + '] (ID:' + str(self.id) + ')'