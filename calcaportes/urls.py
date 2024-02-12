from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('historico/', views.historico, name='historico'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_user, name='logout'),
    path('empleado/<int:id>/', views.empleado, name='empleado'),
    path('exportar_csv/', views.exportar_a_csv, name='exportar'),
    path('register/', views.register_user, name='register'),
    #path('logout/', views.logout_user, name='logout'),
]
