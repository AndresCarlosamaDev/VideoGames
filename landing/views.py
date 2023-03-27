from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import JuegoPopular,JuegoJugador
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .form import JuegoJugadorForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    juegos = JuegoPopular.objects.all()
    return render(request, 'home.html', {'juegos': juegos})


def inicio_sesion(request):
    if request.method == 'GET':
        return render(request, 'inicio_sesion.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                usuario = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                    email=request.POST['correo'])
                nombreUsuario = request.POST['username']
                login(request, usuario)
                usuario.save()
                return redirect("/perfil/" + nombreUsuario)
            except:
                return render(request, 'inicio_sesion.html',{
                    'form': UserCreationForm,
                    'error': "El usuario ya existe"
                    })
        return render(request, 'inicio_sesion.html', {
            'form': UserCreationForm,
            'error': "Contraseñas NO coninciden"
            })
@login_required
def perfil(request, usuario):
    juegos = JuegoJugador.objects.filter(user=request.user)
    
    # CONTADOR JUEGOS
    contador=0
    for i in juegos:
        contador+=1
        print(i)

    return render(request, 'perfil.html', {
        'usuario': usuario,
        'exito': "Usuario registrado satisfactoriamente",
        'juegos': juegos,
        'contador': contador
        })
@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('/')

def reingresar_Sesion(request):
    if request.method == 'GET':
        return render(request, 'reingresar.html',{
            'form': AuthenticationForm
        })
    else:
        usuario = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if usuario is None:
            return render(request, 'reingresar.html',{
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        nombreUsuario = request.POST['username']
        login(request, usuario)
        return redirect("/perfil/" + nombreUsuario)
    
# --------------------------
# JUEGO JUGADOR
# --------------------------
@login_required
def addJuego(request):
    if request.method == 'GET':
        return render(request, 'addJuego.html',{
            'form' : JuegoJugadorForm
    })
    else:
        try:
            form = JuegoJugadorForm(request.POST)
            nuevoJuego = form.save(commit=False)
            nuevoJuego.user = request.user
            #print(nuevoJuego)
            nuevoJuego.save()
            usuario = request.POST['usuario']
            return redirect("/perfil/" + usuario)
        except:
            return render(request, 'addjuego.html',{
            'form' : JuegoJugadorForm,
            'error': 'Valores NO validos'
            })
@login_required
def completar(request,id):
    #print(id)
    nuevoEstado = JuegoJugador.objects.get(id=id)
    nuevoEstado.estado = 'Completado'
    nuevoEstado.save()
    usuario = request.user
    return redirect("/perfil/" + str(usuario))

# ----------------
# TWITCH
# ----------------

def twitch(request):
    return redirect('https://www.twitch.tv/')