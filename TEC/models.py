from django.db import models

class Consecionaria(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    nombreGerente = models.CharField(max_length=100)    

    def __str__(self):
        return "Nombre Consecionaria: %s - Dirección: %s - Nombre del Gerente: %s" % (self.nombre,
                self.direccion,
                self.nombreGerente)
    
class Ponentes(models.Model):
    nombres = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)    
    foto = models.ImageField(upload_to='static/images', blank=True, null=True)

    def __str__(self):
        return "%s - %s -  %s" % (self.nombres,
                self.area,
                self.localidad)
    
class ControlE(models.Model):
    clasificacion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    fecha = models.CharField(max_length=100)    
    mes = models.CharField(max_length=100)
    expositor = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100) 
    tema = models.CharField(max_length=100)
    metodologia = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100) 
    publico = models.CharField(max_length=100)
    reporte = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.clasificacion,
                self.tipo,
                self.fecha,
                self.mes,
                self.expositor,
                self.carrera,
                self.tema,
                self.metodologia,
                self.lugar,
                self.publico,
                self.reporte)

class ExpositoresCon(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    conocimientos = models.CharField(max_length=100)    
    numEventos = models.CharField(max_length=100)
    calificacion = models.CharField(max_length=100)
    presupuesto = models.CharField(max_length=100) 
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100) 
    contacto = models.CharField(max_length=100)

    def __str__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.nombres,
                self.apellidos,
                self.conocimientos,
                self.numEventos,
                self.calificacion,
                self.presupuesto,
                self.correo,
                self.telefono,
                self.ciudad,
                self.contacto)

class Auto(models.Model):
        
    marca = models.CharField(max_length=30)
    añoFab = models.IntegerField()
    costoMin = models.FloatField()
    costoMax = models.FloatField()
    color = models.CharField(max_length=30)
    valorSeguro = models.FloatField()
    
    consecionaria1 = models.ForeignKey(Consecionaria, on_delete=models.CASCADE,
            related_name="autosC")

    def __str__(self):
        return "Marca: %s Año de Fabricación: %s Costo Mínimo: %s Costo Máximo: %s Color: %s Valor del Seguro: %s" % (self.marca,
                self.añoFab,
                self.costoMin,
                self.costoMax,
                self.color,
                self.valorSeguro)
    
class Moto(models.Model):
    tipoM = (
        ('trabajo', 'Trabajo'),
        ('deportiva', 'Deportiva'),
        )
        
    marcaM = models.CharField(max_length=30)
    añoFabM = models.IntegerField()
    valorFijo = models.FloatField()
    tipo = models.CharField(max_length=30, \
                            choices=tipoM)
    
    
    consecionaria2 = models.ForeignKey(Consecionaria, on_delete=models.CASCADE,
            related_name="motosC")

    def __str__(self):
        return "Marca: %s Año de Fabricación: %s Valor Fijo: %s Tipo: %s" % (self.marcaM,
                self.añoFabM,
                self.valorFijo,
                self.tipo)

    
    


