from django.urls import path, include
from .views import *
from .forms import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio" ), 
    path('campera/', campera, name="campera" ), 
    path('chaleco/', chaleco, name="chaleco" ), 
    path('pantalon/', pantalon, name="pantalon" ), 
    path('chaparreras/', chaparreras, name="chaparreras" ),
    path('guantes/', guantes, name="guantes" ),  
    
    path('campera_form/', camperaForm, name="campera_form" ),
    path('chaleco_form/', chalecoForm, name="chaleco_form" ),
    path('pantalon_form/', pantalonForm, name="pantalon_form" ),
    path('chaparreras_form/', chaparrerasForm, name="chaparreras_form" ),
    path('guantes_form/', guantesForm, name="guantes_form" ),
    
    path('buscar_campera/', buscarCampera, name="buscar_campera" ),
    path('buscar2/', buscar2, name="buscar2" ),
    
    path('buscar_chaleco/', buscarChaleco, name="buscar_chaleco" ),
    path('buscar3/', buscar3, name="buscar3" ),
    
    path('buscar_chaparreras/', buscarChaparreras, name="buscar_chaparreras" ),
    path('buscar4/', buscar4, name="buscar4" ),
    
    path('buscar_guantes/', buscarGuantes, name="buscar_guantes" ),
    path('buscar5/', buscar5, name="buscar5" ),
    
    path('buscar_pantalon/', buscarPantalon, name="buscar_pantalon" ),
    path('buscar6/', buscar6, name="buscar6" ),
    
    path('update_campera/<id_campera>/', updateCampera, name="update_campera" ),
    path('delete_campera/<id_campera>/', deleteCampera, name="delete_campera" ),
    path('create_campera/', createCampera, name="create_campera" ),
    
    path('update_pantalon/<id_pantalon>/', updatePantalon, name="update_pantalon" ),
    path('delete_pantalon/<id_pantalon>/', deletePantalon, name="delete_pantalon" ),
    path('create_pantalon/', createPantalon, name="create_pantalon" ),
    
    path('update_chaleco/<id_chaleco>/', updateChaleco, name="update_chaleco" ),
    path('delete_chaleco/<id_chaleco>/', deleteChaleco, name="delete_chaleco" ),
    path('create_chaleco/', createChaleco, name="create_chaleco" ),
    
    path('update_guantes/<id_guantes>/', updateGuantes, name="update_guantes" ),
    path('delete_guantes/<id_guantes>/', deleteGuantes, name="delete_guantes" ),
    path('create_guantes/', createGuantes, name="create_guantes" ),
    
    path('update_chaparreras/<id_chaparreras>/', updateChaparreras, name="update_chaparreras" ),
    path('delete_chaparreras/<id_chaparreras>/', deleteChaparreras, name="delete_chaparreras" ),
    path('create_chaparreras/', createChaparreras, name="create_chaparreras" ),
    
    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="inicio/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),
   
    path('about/', about, name="about" ),
    
]