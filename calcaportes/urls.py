from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('historico/', views.historico, name='historico'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logout_user, name='logout'),
    path('empleado/<int:id>/', views.empleado, name='empleado'),
    #path('logout/', views.logout_user, name='logout'),
]
