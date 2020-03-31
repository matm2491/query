from django.urls import path
from militares.views import soldado_registro
from . import views


urlpatterns = [
    path('', soldado_registro.as_view(template_name= "militares/index.html")),
    path('base', views.base),
   # path('actas/juramentados_leer', juramentados_leer.as_view(template_name = "actas/juramentados/juramentados_leer.html"), name='juramentados_leer'),
]