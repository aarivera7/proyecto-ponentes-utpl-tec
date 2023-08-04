from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from TEC.models import *

class ConsecionariaForm(ModelForm):
    class Meta:
        model = Consecionaria
        fields = ['nombre', 'direccion', 'nombreGerente']
        labels = {
            'nombre': _('Ingrese nombre por favor'),
            'direccion': _('Ingrese direccion por favor'),
            'nombreGerente': _('Ingrese nombre del gerente por favor'),
        }

class ControlEForm(ModelForm):
    class Meta:
        model = ControlE
        fields = ['clasificacion','tipo','fecha','mes','expositor','carrera','tema','metodologia','lugar','publico','reporte']
        
class ExpositoresConForm(ModelForm):
    class Meta:
        model = ExpositoresCon
        fields = ['nombres','apellidos','conocimientos','numEventos','calificacion','presupuesto','correo','telefono','ciudad','contacto']
        
class AutoForm(ModelForm):
    class Meta:
        model = Auto
        fields = ['marca', 'añoFab', 'costoMin', 'costoMax', 'color', 'valorSeguro', 'consecionaria1']   
    
class MotoForm(ModelForm):
    class Meta:
        model = Moto
        fields = ['marcaM', 'añoFabM', 'valorFijo', 'tipo', 'consecionaria2']

class PonentesForm(ModelForm):
    class Meta:
        model = Ponentes
        fields = ['nombres', 'area', 'localidad','foto']