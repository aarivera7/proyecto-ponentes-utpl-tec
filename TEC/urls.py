from django.urls import path

from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('crear/consecionaria', views.crearPonentes, 
            name='crearConsecionaria'),
        path('crear/evento', views.crearControlE, 
            name='crearControlE'),
        path('crear/expositorCon', views.crearExpositoresCon, 
            name='crearExpositoresCon'),
        path('editarConsecionaria/<int:id>', views.editarPonentes, 
            name='editarConsecionaria'),
        path('eliminar/consecionaria/<int:id>', views.eliminarPonentes, 
            name='eliminarConsecionaria'),
        #autos
        path('crear/auto', views.crearAuto, 
            name='crearAuto'),
        path('editar/auto/<int:id>', views.editarAuto, 
            name='editarAuto'),
        path('eliminar/auto/<int:id>', views.eliminarAuto, 
            name='eliminarAuto'),
        #ponentes
        path('ponentes', views.ponentes, 
            name='ponentes'),
        path('estadisticas', views.estadisticas, 
            name='estadisticas'),
 ]
