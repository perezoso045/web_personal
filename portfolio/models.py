from django.db import models

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Titulo" )
    description =models.TextField(verbose_name = "Descripción")
    image = models.ImageField(verbose_name = "Imagen", upload_to = "projects")
    link = models.URLField(blank = True, null = True, max_length=200, verbose_name = "Mas información")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")
   
    
    #configuracion al español de la ventana admin
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]
        
    def __str__(self): #para agregar el nombre del proyecto
	    return self.title 
