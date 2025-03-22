from django.urls import path
from .views import actualizar_orden, agregar_dispositivo_por_ip, agregar_multiples_dispositivos, agregar_ruta_definida, analizar_ruta, buscar_dispositivo, editar_ruta, eliminar_dispositivo_ruta_definida, eliminar_ruta, formulario_agregar_ruta_definida, inventario_por_ubicacion, mostrar_animacion, obtener_dispositivos_ruta, ping_ruta, verificar_estado_dispositivo, mostrar_grafica, monitoreo_red, agregar_ruta, lista_rutas

urlpatterns = [
    path('monitoreo_red', monitoreo_red, name='analizar_ruta'), #INTERFAZ
    path("analizar_ruta/", analizar_ruta, name="analizar_ruta"),
    path('inventario/', inventario_por_ubicacion, name='inventario'), #INTERFAZ
    path('verificar_estado/', verificar_estado_dispositivo, name='verificar_estado'),

    path('ruta/agregar/ruta_definida', formulario_agregar_ruta_definida, name='formulario_agregar_ruta'), #INTERFAZ
    path("ruta/agregar/", agregar_ruta_definida, name="agregar_ruta"),
    path('editar_ruta/<int:id_ruta>/', editar_ruta, name='editar_ruta'),

    path('ruta/<int:id_ruta>/eliminar-dispositivo/<int:id_dispositivo>/', eliminar_dispositivo_ruta_definida, name='eliminar_dispositivo_ruta_definida'),
    path('ruta/<int:id_ruta>/agregar-dispositivo/', agregar_dispositivo_por_ip, name='agregar_dispositivo_por_ip'),
    path('buscar-dispositivo/', buscar_dispositivo, name='buscar_dispositivo'),
    path('ruta/<int:id_ruta>/agregar-multiples-dispositivos/', agregar_multiples_dispositivos, name='agregar_multiples_dispositivos'),
    path('ruta/<int:id_ruta>/dispositivos/', obtener_dispositivos_ruta, name="obtener_dispositivos_ruta"),
    path('ruta/<int:id_ruta>/actualizar-orden/', actualizar_orden, name='actualizar-orden'),
    

    path('ping_ruta/<int:id_ruta>/', ping_ruta, name='ping_ruta'),
    path('verificar_estado/<str:ip>/', verificar_estado_dispositivo, name='verificar_estado_dispositivo'),

    

    path('lista_rutas/', lista_rutas, name='lista_rutas'), #INTERFAZ

    path('eliminar_ruta/<int:id_ruta>/', eliminar_ruta, name='eliminar_ruta'),






    path('grafica/', mostrar_grafica, name='mostrar_grafica'),
    path('animacion/', mostrar_animacion, name='mostrar_animacion'),
]
