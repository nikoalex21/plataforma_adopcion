from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Perfil, Animalito, SolicitudAdopcion, Donacion, Ayuda
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import DonacionForm, AyudaForm

@login_required
def vista_veterinario(request):
    # Obtener todos los animalitos, junto con los datos del ayudador
    animalitos = Animalito.objects.select_related('ayudador').all()

    if request.method == 'POST':
        animalito_id = request.POST.get('animalito_id')
        nuevo_estado = request.POST.get('nuevo_estado')
        descripcion_veterinario = request.POST.get('descripcion_veterinario') 
        try:
            animalito = Animalito.objects.get(id=animalito_id)
            animalito.estado = nuevo_estado
            animalito.descripcion_veterinario = descripcion_veterinario 
            animalito.usuario_actualizador = request.user 
            if not animalito.estado:
             animalito.estado = 'Estado predeterminado'
            animalito.save()
            return redirect('vista_veterinario')  
        except Animalito.DoesNotExist:
            return HttpResponse("Error: Animalito no encontrado.")

    return render(request, 'veterinario.html', {'animalitos': animalitos})



@login_required
def vista_hogar_paso(request):
    
    perfil = Perfil.objects.get(user=request.user)

   
    animales_a_cargo = Animalito.objects.filter(ayudador=perfil)

    return render(request, 'hogar_paso.html', { 'animales_a_cargo': animales_a_cargo,    })


def vista_adoptante(request):
    return render(request, 'adoptante.html')

def vista_colaborador(request):
    return render(request, 'colaborador.html')

def vista_ayudador(request):
    return render(request, 'ayudador.html')

def home(request):
    return render(request, 'home.html')


def registro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cedula = request.POST.get('cedula')
        telefono = request.POST.get('telefono')
        rol = request.POST.get('rol')

        
        if User.objects.filter(username=username).exists():
            return HttpResponse("Error: El nombre de usuario ya existe. Elige otro.")
        
        try:
            # Crear el usuario
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            
            perfil = Perfil.objects.create(user=user, cedula=cedula, telefono=telefono, rol=rol)
            perfil.save()

           
            return redirect('registrado')  

        except IntegrityError:
            return HttpResponse("Error: No se pudo crear el usuario. Intenta de nuevo.")
    
    return render(request, 'registro.html')  

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Obtener el perfil y redirigir según el rol
            try:
                perfil = Perfil.objects.get(user=user)
                if perfil.rol == 'veterinario':
                    return redirect('vista_veterinario') 
                elif perfil.rol == 'hogar_paso':
                    return redirect('vista_hogar_paso')  
                elif perfil.rol == 'adoptante':
                    return redirect('vista_adoptante') 
                elif perfil.rol == 'colaborador':
                    return redirect('vista_colaborador')  
                elif perfil.rol == 'ayudador':
                    return redirect('vista_ayudador') 
                else:
                    return redirect('home')  

            except Perfil.DoesNotExist:
                return HttpResponse("Error: Perfil no encontrado.")

        else:
            return HttpResponse("Error: Nombre de usuario o contraseña incorrectos.")

    return render(request, 'login.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['nombre_usuario'] = user.first_name  # Guarda el nombre en la sesión
            
            # Guarda el tipo de usuario en la sesión
            if hasattr(user, 'ayudador'):  
                request.session['tipo_usuario'] = 'ayudador'
            elif hasattr(user, 'adoptante'):
                request.session['tipo_usuario'] = 'adoptante'
            elif hasattr(user, 'veterinario'):
                request.session['tipo_usuario'] = 'veterinario'
            elif hasattr(user, 'hogar_de_paso'):
                request.session['tipo_usuario'] = 'hogar_de_paso'
            else:
                request.session['tipo_usuario'] = 'invitado' 

            return redirect('home')  
    return render(request, 'iniciar_sesion.html')

@login_required
def registrar_animalito(request):
    if request.method == 'POST':
      
        perfil = Perfil.objects.get(user=request.user)

        
        animalito = Animalito(
            nombre=request.POST.get('nombre'),
            especie=request.POST.get('especie'),
            edad=request.POST.get('edad'),
            descripcion=request.POST.get('descripcion'),
            imagen=request.FILES.get('imagen'),
            estado=request.POST.get('estado'), 
            ayudador=perfil
        )
        animalito.save()

        return redirect('vista_ayudador')

    return render(request, 'registrar_animalito.html')


@login_required
def seguimiento_animalitos(request):
   
    perfil = Perfil.objects.get(user=request.user)

   
    animalitos = Animalito.objects.filter(ayudador=perfil)

    ayudadores = Perfil.objects.filter(rol='ayudador')

    
    return render(request, 'seguimiento_animalitos.html', {
        'animalitos': animalitos,
        'ayudadores': ayudadores,  
    })

@login_required
def ver_animalitos(request):
   
    perfil = Perfil.objects.get(user=request.user)

    
    animales_a_cargo = Animalito.objects.filter(ayudador=perfil)

    return render(request, 'ver_animalitos.html', {
        'animales_a_cargo': animales_a_cargo,
    })

@login_required
def recoger_animalito(request):

    animales_en_calle = Animalito.objects.filter(Q(estado='calle') | Q(estado='revisado_veterinario')) 

    if request.method == 'POST':
        
        animalito_id = request.POST.get('animalito_id')
        animalito = Animalito.objects.get(id=animalito_id)
        perfil = Perfil.objects.get(user=request.user)

       
        animalito.estado = 'en_hogar_paso'  
        animalito.ayudador = perfil
        animalito.save()

        return redirect('vista_hogar_paso')  

    return render(request, 'recoger_animalito.html', {
        'animales_en_calle': animales_en_calle,
    })

@login_required
def hogares_de_paso_view(request):
   
    hogares_paso = Perfil.objects.filter(rol='hogar_paso')
    
   
    print(hogares_paso)  

    return render(request, 'hogares_de_paso.html', {'hogares_paso': hogares_paso})

@login_required
def animales_en_hogar(request, hogar_id):
    hogar = get_object_or_404(Perfil.objects.filter(rol='hogar_paso'), id=hogar_id)  
    animales = Animalito.objects.filter(ayudador=hogar)
    

    return render(request, 'animales_en_hogar.html', {
        'hogar': hogar,
        'animales': animales,
    })

@login_required
def solicitar_adopcion(request, animal_id):
    animal = get_object_or_404(Animalito, id=animal_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        edad = request.POST.get('edad')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        direccion = request.POST.get('direccion')

        # Validar que los campos no estén vacíos
        if not (nombre and edad and correo and telefono and direccion):
            return render(request, 'solicitar_adopcion.html', {'animal': animal, 'error': 'Todos los campos son obligatorios.'})

        # Crear y guardar la solicitud de adopción
        solicitud = SolicitudAdopcion.objects.create(
            animal=animal,
            adoptante=request.user,  
            nombre=nombre,
            edad=edad,
            correo_electronico=correo,
            telefono=telefono,
            direccion=direccion,
            estado='pendiente'
        )

        
        return redirect('vista_solicitud_enviada')
    
    return render(request, 'solicitar_adopcion.html', {'animal': animal})


@login_required
def listar_solicitudes(request):
    
    solicitudes = SolicitudAdopcion.objects.filter(estado='pendiente')

    
    return render(request, 'listar_solicitudes.html', {
        'solicitudes': solicitudes  
    })


@login_required
def aprobar_rechazar_solicitud(request, solicitud_id):
   
    solicitud = get_object_or_404(SolicitudAdopcion, id=solicitud_id)

    if request.method == 'POST':
        
        decision = request.POST.get('decision')

        
        solicitud.estado = decision
        solicitud.save()

        
        if decision == 'aprobada':
            animalito = solicitud.animal 
            animalito.estado = 'adoptado'  
            animalito.hogar = solicitud.adoptante.perfil  
            animalito.save()

    
    return redirect('listar_solicitudes')


def vista_solicitud_enviada(request):
    return render(request, 'solicitud_enviada.html')

@login_required
def donar(request):
    return render(request, 'donar.html')

@login_required
def registrar_ayuda(request):
    if request.method == 'POST':
        form = AyudaForm(request.POST)
        if form.is_valid():
            ayuda = form.save()
            return redirect('gracias_por_ayudar')  
    else:
        form = AyudaForm()
    return render(request, 'registrar_ayuda.html', {'form': form})

def gracias_por_ayudar(request):
    return render(request, 'gracias_por_ayudar.html')

@login_required
def seguimiento_ayudas(request):
    donaciones = Donacion.objects.all() 
    ayudas = Ayuda.objects.all()  

    return render(request, 'seguimiento_ayudas.html', {
        'donaciones': donaciones,
        'ayudas': ayudas
    })
