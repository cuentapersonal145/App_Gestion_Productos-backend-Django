from django.db import models

class Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    codigo_barras = models.CharField(max_length=64, null=False, blank=False)
    detalle = models.CharField(max_length=255, null=False, blank=False)
    precio = models.PositiveIntegerField()
    
    date_record = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['detalle']
        verbose_name = ("Articulo")
        verbose_name_plural = ("Articulos")
        db_table = 'ARTICULO'
        
    def __str__(self):
        return self.detalle + ' : $' + str(self.precio) + '. [CD:' + self.codigo_barras + '] (ID:' + str(self.id) + ')'