from django import views
from django.urls import URLPattern, path
from . import views

app_name = 'sistema_2'

urlpatterns = [
    path('',views.login_view,name='login_view'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('servicios',views.servicios,name='servicios'),
    path('clientes',views.clientes,name='clientes'),
    path('productos',views.productos,name='productos'),
    path('proformas',views.proformas,name='proformas'),
    path('usuarios',views.usuarios,name='usuarios'),
    path('facturas',views.facturas,name='facturas'),
    path('guias',views.guias,name='guias'),
    path('add_client',views.add_client,name='add_client'),
    path('add_product',views.add_product,name='add_product'),
    path('add_service',views.add_service,name='add_service'),
    path('add_user',views.add_user,name='add_user'),
    path('add_proforma',views.add_proforma,name='add_proforma'),
    path('add_producto_proforma',views.add_producto_proforma,name='add_producto_proforma'),
    path('add_cliente_proforma',views.add_cliente_proforma,name='add_cliente_proforma'),
    path('generar_proforma/<str:ind>',views.generar_proforma,name='generar_proforma'),
    path('descargar_guia/<str:ind>',views.descargar_guia,name='descargar_guia'),
    path('descargar_factura/<str:ind>',views.descargar_factura,name='descargar_factura'),
    path('crear_guia',views.crear_guia,name='crear_guia'),
    path('crear_factura',views.crear_factura,name='crear_factura'),
    path('eliminar_usuario/<str:ind>',views.eliminar_usuario,name='eliminar_usuario'),
    path('update_user/<str:ind>',views.update_user,name='update_user'),
    path('eliminar_producto/<str:ind>',views.eliminar_producto,name='eliminar_producto'),
    path('update_product/<str:ind>',views.update_product,name='update_product'),
    path('eliminar_servicio/<str:ind>',views.eliminar_servicio,name='eliminar_servicio'),
    path('update_service/<str:ind>',views.update_service,name='update_service'),
    path('eliminar_cliente/<str:ind>',views.eliminar_cliente,name='eliminar_cliente'),
    path('update_client/<str:ind>',views.update_client,name='update_client'),
    path('eliminar_proforma/<str:ind>',views.eliminar_proforma,name='eliminar_proforma'),
    path('importar_usuarios',views.importar_usuarios,name='importar_usuarios'),
    path('importar_clientes',views.importar_clientes,name='importar_clientes'),
    path('importar_productos',views.importar_productos,name='importar_productos'),
    path('importar_servicios',views.importar_servicios,name='importar_servicios'),
    path('generar_guia/<str:ind>',views.generar_guia,name='generar_guia'),
    path('generar_factura/<str:ind>',views.generar_factura,name='generar_factura'),
    path('log_out',views.log_out,name='log_out'),
    path('add_stock/<str:ind>',views.add_stock,name='add_stock'),
    path('ver_factura/<str:ind>',views.ver_factura,name='ver_factura'),
    path('ver_proforma/<str:ind>',views.ver_proforma,name='ver_proforma'),
]