from django.urls import path
from .views import registro_view
from django.views.generic import TemplateView
from .views import (
    login_view,
    vista_veterinario,
    vista_hogar_paso,
    vista_adoptante,
    vista_colaborador,
    vista_ayudador,
    home,
    registrar_animalito, seguimiento_animalitos, recoger_animalito,ver_animalitos, hogares_de_paso_view, animales_en_hogar,
    solicitar_adopcion, listar_solicitudes, aprobar_rechazar_solicitud, vista_solicitud_enviada, donar,registrar_ayuda,seguimiento_ayudas,
    gracias_por_ayudar
)


urlpatterns = [
    path('registro/', registro_view, name='registro'),
    path('registrado/', TemplateView.as_view(template_name='registrado.html'), name='registrado'),
    path('login/', login_view, name='login'),
    path('veterinario/', vista_veterinario, name='vista_veterinario'),
    path('hogar_paso/', vista_hogar_paso, name='vista_hogar_paso'),
    path('adoptante/', vista_adoptante, name='vista_adoptante'),
    path('colaborador/', vista_colaborador, name='vista_colaborador'),
    path('ayudador/', vista_ayudador, name='vista_ayudador'),
    path('', home, name='home'),
    path('registrar-animalito/', registrar_animalito, name='registrar_animalito'),
    path('seguimiento-animalitos/', seguimiento_animalitos, name='seguimiento_animalitos'),
    path('recoger-animalito/', recoger_animalito, name='recoger_animalito'),
    path('ver-animalito/', ver_animalitos, name='ver_animalitos'),
    path('hogares_de_paso/', hogares_de_paso_view, name='hogares_de_paso'),
    path('hogar/<int:hogar_id>/animales/', animales_en_hogar, name='animales_en_hogar'),
    path('adoptar/solicitar/<int:animal_id>/', solicitar_adopcion, name='solicitar_adopcion'),
    path('hogar/solicitudes/', listar_solicitudes, name='listar_solicitudes'),
    path('hogar/solicitudes/<int:solicitud_id>/decidir/', aprobar_rechazar_solicitud, name='aprobar_rechazar_solicitud'),
    path('solicitud-enviada/', vista_solicitud_enviada, name='vista_solicitud_enviada'),
    path('donar/', donar, name='donar'),
    path('registrar_ayuda/', registrar_ayuda, name='registrar_ayuda'),
    path('seguimiento_ayudas/', seguimiento_ayudas, name='seguimiento_ayudas'),
     path('gracias_por_ayudar/', gracias_por_ayudar, name='gracias_por_ayudar'),

]
