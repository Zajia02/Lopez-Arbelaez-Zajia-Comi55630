from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.urls import reverse_lazy



from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def inicio(request):
    return render(request, "inicio/inicio.html")
   

@login_required
def campera(request):
    contexto = {'campera': Campera.objects.all() }
    return render(request, "inicio/campera.html", contexto)

@login_required
def chaleco(request):
    contexto = {'chaleco': Chaleco.objects.all() }
    return render(request, "inicio/chaleco.html", contexto)

@login_required
def pantalon(request):
    contexto = {'pantalon': Pantalon.objects.all() }
    return render(request, "inicio/pantalon.html", contexto)

@login_required
def chaparreras(request):
    contexto = {'chaparreras': Chaparreras.objects.all() }
    return render(request, "inicio/chaparreras.html", contexto)

@login_required
def guantes(request):
    contexto = {'guantes': Guantes.objects.all() }
    return render(request, "inicio/guantes.html", contexto)

# Formularios de agregación

@login_required
def camperaForm(request):
    if request.method == "POST":
        miForm = CamperaForm(request.POST)
        if miForm.is_valid():
            campera_talle = miForm.cleaned_data.get('talle')
            campera_color1 = miForm.cleaned_data.get('color1')
            campera_color2 = miForm.cleaned_data.get('color2')
            campera_modelo = miForm.cleaned_data.get('modelo')
            campera = Campera(talle=campera_talle,
                              color1=campera_color1,
                              color2=campera_color2,
                              modelo=campera_modelo)
            campera.save()
            return HttpResponse("Se agregó la campera con éxito")
            return render(request, "inicio/base.html")
    else:
        miForm = CamperaForm()
        
    return render(request, "inicio/camperaForm.html", {"form": miForm})

@login_required
def chalecoForm(request):
    if request.method == "POST":
        miForm = ChalecoForm(request.POST)
        if miForm.is_valid():
            chaleco_talle = miForm.cleaned_data.get('talle')
            chaleco_color1 = miForm.cleaned_data.get('color1')
            chaleco_color2 = miForm.cleaned_data.get('color2')
            chaleco_modelo = miForm.cleaned_data.get('modelo')
            chaleco = Chaleco(talle=chaleco_talle,
                              color1=chaleco_color1,
                              color2=chaleco_color2,
                              modelo=chaleco_modelo)
            chaleco.save()
            return HttpResponse("Se agregó el chaleco con éxito")
            return render(request, "inicio/base.html")
    else:
        miForm = ChalecoForm()
        
    return render(request, "inicio/chalecoForm.html", {"form": miForm})

@login_required
def chaparrerasForm(request):
    if request.method == "POST":
        miForm = ChaparrerasForm(request.POST)
        if miForm.is_valid():
            chaparreras_talle = miForm.cleaned_data.get('talle')
            chaparreras_color1 = miForm.cleaned_data.get('color1')
            chaparreras_color2 = miForm.cleaned_data.get('color2')
            chaparreras_modelo = miForm.cleaned_data.get('modelo')
            chaparreras = Chaparreras(talle=chaparreras_talle,
                              color1=chaparreras_color1,
                              color2=chaparreras_color2,
                              modelo=chaparreras_modelo)
            chaparreras.save()
            return HttpResponse("Se agregaron las chaparreras con éxito")
            return render(request, "inicio/base.html")
    else:
        miForm = ChaparrerasForm()
        
    return render(request, "inicio/chaparrerasForm.html", {"form": miForm})

@login_required
def guantesForm(request):
    if request.method == "POST":
        miForm = GuantesForm(request.POST)
        if miForm.is_valid():
            guantes_talle = miForm.cleaned_data.get('talle')
            guantes_color1 = miForm.cleaned_data.get('color1')
            guantes_color2 = miForm.cleaned_data.get('color2')
            guantes_modelo = miForm.cleaned_data.get('modelo')
            guantes = Guantes(talle=guantes_talle,
                              color1=guantes_color1,
                              color2=guantes_color2,
                              modelo=guantes_modelo)
            guantes.save()
            return HttpResponse("Se agregaron los guantes con éxito")
            return render(request, "inicio/base.html")
    else:
        miForm = GuantesForm()
        
    return render(request, "inicio/guantesForm.html", {"form": miForm})

@login_required
def pantalonForm(request):
    if request.method == "POST":
        miForm = PantalonForm(request.POST)
        if miForm.is_valid():
            pantalon_talle = miForm.cleaned_data.get('talle')
            pantalon_color1 = miForm.cleaned_data.get('color1')
            pantalon_color2 = miForm.cleaned_data.get('color2')
            pantalon_modelo = miForm.cleaned_data.get('modelo')
            pantalon = Pantalon(talle=pantalon_talle,
                              color1=pantalon_color1,
                              color2=pantalon_color2,
                              modelo=pantalon_modelo)
            pantalon.save()
            return HttpResponse("Se agregó el pantalón con éxito")
            return render(request, "inicio/base.html")
    else:
        miForm = PantalonForm()
        
    return render(request, "inicio/pantalonForm.html", {"form": miForm})
    

# Formularios de Búsqueda

@login_required
def buscarCampera(request):
    return render(request, "inicio/buscarCampera.html")

@login_required
def buscar2(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_campera = Campera.objects.filter(talle__icontains=patron)
        color1_campera = Campera.objects.filter(color1__icontains=patron)
        color2_campera = Campera.objects.filter(color2__icontains=patron)
        modelo_campera = Campera.objects.filter(modelo__icontains=patron)

        if talle_campera:
            contexto = {'campera': talle_campera}
        elif color1_campera:
            contexto = {'campera': color1_campera}
        elif color2_campera:
            contexto = {'campera': color2_campera}
        elif modelo_campera:
            contexto = {'campera': modelo_campera}
        else:
            return HttpResponse("No se encontraron camperas")   

        return render(request, "inicio/campera.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")

@login_required
def buscarChaleco(request):
    return render(request, "inicio/buscarChaleco.html")

@login_required
def buscar3(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_chaleco = Chaleco.objects.filter(talle__icontains=patron)
        color1_chaleco = Chaleco.objects.filter(color1__icontains=patron)
        color2_chaleco = Chaleco.objects.filter(color2__icontains=patron)
        modelo_chaleco = Chaleco.objects.filter(modelo__icontains=patron)

        if talle_chaleco:
            contexto = {'chaleco': talle_chaleco}
        elif color1_chaleco:
            contexto = {'chaleco': color1_chaleco}
        elif color2_chaleco:
            contexto = {'chaleco': color2_chaleco}
        elif modelo_chaleco:
            contexto = {'chaleco': modelo_chaleco}
        else:
            return HttpResponse("No se encontraron chalecos")    

        return render(request, "inicio/chaleco.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")

@login_required    
def buscarChaparreras(request):
    return render(request, "inicio/buscarChaparreras.html")

@login_required
def buscar4(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_chaparreras = Chaparreras.objects.filter(talle__icontains=patron)
        color1_chaparreras = Chaparreras.objects.filter(color1__icontains=patron)
        color2_chaparreras = Chaparreras.objects.filter(color2__icontains=patron)
        modelo_chaparreras = Chaparreras.objects.filter(modelo__icontains=patron)

        if talle_chaparreras:
            contexto = {'chaparreras': talle_chaparreras}
        elif color1_chaparreras:
            contexto = {'chaparreras': color1_chaparreras}
        elif color2_chaparreras:
            contexto = {'chaparreras': color2_chaparreras}
        elif modelo_chaparreras:
            contexto = {'chaparreras': modelo_chaparreras}
        else:
            return HttpResponse("No se encontraron chaparreras")    

        return render(request, "inicio/chaparreras.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")

@login_required   
def buscarGuantes(request):
    return render(request, "inicio/buscarGuantes.html")

@login_required
def buscar5(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_guantes = Guantes.objects.filter(talle__icontains=patron)
        color1_guantes = Guantes.objects.filter(color1__icontains=patron)
        color2_guantes = Guantes.objects.filter(color2__icontains=patron)
        modelo_guantes = Guantes.objects.filter(modelo__icontains=patron)

        if talle_guantes:
            contexto = {'guantes': talle_guantes}
        elif color1_guantes:
            contexto = {'guantes': color1_guantes}
        elif color2_guantes:
            contexto = {'guantes': color2_guantes}
        elif modelo_guantes:
            contexto = {'guantes': modelo_guantes}
        else:
            return HttpResponse("No se encontraron guantes")    

        return render(request, "inicio/guantes.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")

@login_required
def buscarPantalon(request):
    return render(request, "inicio/buscarPantalon.html")    

@login_required    
def buscar6(request):
    patron = request.GET.get('buscar') # Usar request.GET.get() para evitar KeyError

    if patron:
        talle_pantalon = Pantalon.objects.filter(talle__icontains=patron)
        color1_pantalon = Pantalon.objects.filter(color1__icontains=patron)
        color2_pantalon = Pantalon.objects.filter(color2__icontains=patron)
        modelo_pantalon = Pantalon.objects.filter(modelo__icontains=patron)

        if talle_pantalon:
            contexto = {'pantalon': talle_pantalon}
        elif color1_pantalon:
            contexto = {'pantalon': color1_pantalon}
        elif color2_pantalon:
            contexto = {'pantalon': color2_pantalon}
        elif modelo_pantalon:
            contexto = {'pantalon': modelo_pantalon}
        else:
            return HttpResponse("No se encontraron pantalones")    

        return render(request, "inicio/pantalon.html", contexto)
    else:
        return HttpResponse("No se ingresó nada en buscar")        


@login_required        
def updateCampera(request, id_campera):
    campera = Campera.objects.get(id=id_campera)
    if request.method == "POST":
        miForm = CamperaForm(request.POST)
        if miForm.is_valid():
            campera.talle = miForm.cleaned_data.get('talle')
            campera.color1 = miForm.cleaned_data.get('color1')
            campera.color2 = miForm.cleaned_data.get('color2')
            campera.modelo = miForm.cleaned_data.get('modelo')
            campera.save()
            return redirect(reverse_lazy('campera'))
    else:
        miForm = CamperaForm(initial={
            'talle': campera.talle,
            'color1': campera.color1,
            'color2': campera.color2,
            'modelo': campera.modelo,
        }) 
    return render(request, "inicio/camperaForm.html", {'form': miForm})   

@login_required
def deleteCampera(request, id_campera):
    campera = Campera.objects.get(id=id_campera)
    if request.method == 'GET':
        return render(request, "inicio/campera_confirm_delete.html", {'id_campera':id_campera})
    else:
        campera.delete() 
        return redirect(reverse_lazy('campera'))

@login_required
def createCampera(request):
    if request.method == "POST":
        miForm = CamperaForm(request.POST)
        if miForm.is_valid():
            c_talle = miForm.cleaned_data.get('talle')
            c_color1 = miForm.cleaned_data.get('color1')
            c_color2 = miForm.cleaned_data.get('color2')
            c_modelo = miForm.cleaned_data.get('modelo')
            campera = Campera(talle=c_talle,
                            color1=c_color1,
                            color2=c_color2,
                            modelo=c_modelo,
                            )
            campera.save()
            return redirect(reverse_lazy('campera'))
    else:
        miForm = CamperaForm() 
        
    return render(request, "inicio/camperaForm.html", {'form': miForm}) 

@login_required
def updatePantalon(request, id_pantalon):
    pantalon = Pantalon.objects.get(id=id_pantalon)
    if request.method == "POST":
        miForm = PantalonForm(request.POST)
        if miForm.is_valid():
            pantalon.talle = miForm.cleaned_data.get('talle')
            pantalon.color1 = miForm.cleaned_data.get('color1')
            pantalon.color2 = miForm.cleaned_data.get('color2')
            pantalon.modelo = miForm.cleaned_data.get('modelo')
            pantalon.save()
            return redirect(reverse_lazy('pantalon'))
    else:
        miForm = PantalonForm(initial={
            'talle': pantalon.talle,
            'color1': pantalon.color1,
            'color2': pantalon.color2,
            'modelo': pantalon.modelo,
        }) 
    return render(request, "inicio/pantalonForm.html", {'form': miForm})   

@login_required
def deletePantalon(request, id_pantalon):
    pantalon = Pantalon.objects.get(id=id_pantalon)
    if request.method == 'GET':
        return render(request, "inicio/pantalon_confirm_delete.html", {'id_pantalon':id_pantalon})
    else:
        pantalon.delete() 
        return redirect(reverse_lazy('pantalon'))

@login_required
def createPantalon(request):
    if request.method == "POST":
        miForm = PantalonForm(request.POST)
        if miForm.is_valid():
            c_talle = miForm.cleaned_data.get('talle')
            c_color1 = miForm.cleaned_data.get('color1')
            c_color2 = miForm.cleaned_data.get('color2')
            c_modelo = miForm.cleaned_data.get('modelo')
            pantalon = Pantalon(talle=c_talle,
                            color1=c_color1,
                            color2=c_color2,
                            modelo=c_modelo,
                            )
            pantalon.save()
            return redirect(reverse_lazy('pantalon'))
    else:
        miForm = PantalonForm() 
        
    return render(request, "inicio/pantalonForm.html", {'form': miForm}) 

@login_required
def updateChaleco(request, id_chaleco):
    chaleco = Chaleco.objects.get(id=id_chaleco)
    if request.method == "POST":
        miForm = ChalecoForm(request.POST)
        if miForm.is_valid():
            chaleco.talle = miForm.cleaned_data.get('talle')
            chaleco.color1 = miForm.cleaned_data.get('color1')
            chaleco.color2 = miForm.cleaned_data.get('color2')
            chaleco.modelo = miForm.cleaned_data.get('modelo')
            chaleco.save()
            return redirect(reverse_lazy('chaleco'))
    else:
        miForm = ChalecoForm(initial={
            'talle': chaleco.talle,
            'color1': chaleco.color1,
            'color2': chaleco.color2,
            'modelo': chaleco.modelo,
        }) 
    return render(request, "inicio/chalecoForm.html", {'form': miForm})   

@login_required
def deleteChaleco(request, id_chaleco):
    chaleco = Chaleco.objects.get(id=id_chaleco)
    if request.method == 'GET':
        return render(request, "inicio/chaleco_confirm_delete.html", {'id_chaleco':id_chaleco})
    else:
        chaleco.delete() 
        return redirect(reverse_lazy('chaleco'))

@login_required
def createChaleco(request):
    if request.method == "POST":
        miForm = ChalecoForm(request.POST)
        if miForm.is_valid():
            c_talle = miForm.cleaned_data.get('talle')
            c_color1 = miForm.cleaned_data.get('color1')
            c_color2 = miForm.cleaned_data.get('color2')
            c_modelo = miForm.cleaned_data.get('modelo')
            chaleco = Chaleco(talle=c_talle,
                            color1=c_color1,
                            color2=c_color2,
                            modelo=c_modelo,
                            )
            chaleco.save()
            return redirect(reverse_lazy('chaleco'))
    else:
        miForm = ChalecoForm() 
        
    return render(request, "inicio/chalecoForm.html", {'form': miForm}) 

@login_required
def updateGuantes(request, id_guantes):
    guantes = Guantes.objects.get(id=id_guantes)
    if request.method == "POST":
        miForm = GuantesForm(request.POST)
        if miForm.is_valid():
            guantes.talle = miForm.cleaned_data.get('talle')
            guantes.color1 = miForm.cleaned_data.get('color1')
            guantes.color2 = miForm.cleaned_data.get('color2')
            guantes.modelo = miForm.cleaned_data.get('modelo')
            guantes.save()
            return redirect(reverse_lazy('guantes'))
    else:
        miForm = GuantesForm(initial={
            'talle': guantes.talle,
            'color1': guantes.color1,
            'color2': guantes.color2,
            'modelo': guantes.modelo,
        }) 
    return render(request, "inicio/guantesForm.html", {'form': miForm})   

@login_required
def deleteGuantes(request, id_guantes):
    guantes = Guantes.objects.get(id=id_guantes)
    if request.method == 'GET':
        return render(request, "inicio/guantes_confirm_delete.html", {'id_guantes':id_guantes})
    else:
        guantes.delete() 
        return redirect(reverse_lazy('guantes'))

@login_required
def createGuantes(request):
    if request.method == "POST":
        miForm = GuantesForm(request.POST)
        if miForm.is_valid():
            c_talle = miForm.cleaned_data.get('talle')
            c_color1 = miForm.cleaned_data.get('color1')
            c_color2 = miForm.cleaned_data.get('color2')
            c_modelo = miForm.cleaned_data.get('modelo')
            guantes = Guantes(talle=c_talle,
                            color1=c_color1,
                            color2=c_color2,
                            modelo=c_modelo,
                            )
            guantes.save()
            return redirect(reverse_lazy('guantes'))
    else:
        miForm = GuantesForm() 
        
    return render(request, "inicio/guantesForm.html", {'form': miForm}) 

@login_required
def updateChaparreras(request, id_chaparreras):
    chaparreras = Chaparreras.objects.get(id=id_chaparreras)
    if request.method == "POST":
        miForm = ChaparrerasForm(request.POST)
        if miForm.is_valid():
            chaparreras.talle = miForm.cleaned_data.get('talle')
            chaparreras.color1 = miForm.cleaned_data.get('color1')
            chaparreras.color2 = miForm.cleaned_data.get('color2')
            chaparreras.modelo = miForm.cleaned_data.get('modelo')
            chaparreras.save()
            return redirect(reverse_lazy('chaparreras'))
    else:
        miForm = ChaparrerasForm(initial={
            'talle': chaparreras.talle,
            'color1': chaparreras.color1,
            'color2': chaparreras.color2,
            'modelo': chaparreras.modelo,
        }) 
    return render(request, "inicio/chaparrerasForm.html", {'form': miForm})   

@login_required
def deleteChaparreras(request, id_chaparreras):
    chaparreras = Chaparreras.objects.get(id=id_chaparreras)
    if request.method == 'GET':
        return render(request, "inicio/chaparreras_confirm_delete.html", {'id_chaparreras':id_chaparreras})
    else:
        chaparreras.delete() 
        return redirect(reverse_lazy('chaparreras'))

@login_required
def createChaparreras(request):
    if request.method == "POST":
        miForm = ChaparrerasForm(request.POST)
        if miForm.is_valid():
            c_talle = miForm.cleaned_data.get('talle')
            c_color1 = miForm.cleaned_data.get('color1')
            c_color2 = miForm.cleaned_data.get('color2')
            c_modelo = miForm.cleaned_data.get('modelo')
            chaparreras = Chaparreras(talle=c_talle,
                            color1=c_color1,
                            color2=c_color2,
                            modelo=c_modelo,
                            )
            chaparreras.save()
            return redirect(reverse_lazy('chaparreras'))
    else:
        miForm = ChaparrerasForm() 
        
    return render(request, "inicio/chaparrerasForm.html", {'form': miForm})

#__________________ Login / Logout / Registracion
# 
def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:                
                login(request, user)
                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                    
                return redirect("inicio")
            else:
                return render(request, "inicio/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "inicio/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "inicio/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "inicio/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "inicio/registro.html", {"form":miForm}) 

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,"inicio/base.html")
        else:
            return render(request,"inicio/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "inicio/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"inicio/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "inicio/agregarAvatar.html", {'form': form })    

def about(request):
    return render(request, "inicio/about.html") 



     