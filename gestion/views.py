from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
from django.shortcuts import render, redirect, render_to_response
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from gestion.models import Libro, Prestamo, LugarPrestamo
from gestion.forms import UserForm, UsuarioForm, LugaresPrestamoForm

class LibrosList(ListView):
    model = Libro
    template_name = 'gestion/libro_list.html'
    context_object_name = 'libros'
    paginate_by = 5
    
    # def reservarLibro(self, request):
    #     print('Hola')
    #     return None
    def get_queryset(self):
        return Libro.objects.exclude(stock=0)


def confirmar_prestamo(request, pk):
    if request.method == 'POST':
        detalles_prestamo = Libro.objects.filter(pk=pk)
        lugar = LugarPrestamo.objects.filter(nombre="SALA")
        #lugar = request.POST.get('lugar', "SALA")        
        # si el lugar es SALA el tiempo son 3h, cuando añadamos domicilio se considerarán 3 días
        fechaEntrega = datetime.datetime.now() + datetime.timedelta(hours=3)
        Prestamo.objects.create(usuario=request.user, libro = detalles_prestamo[0], lugar = lugar[0] , fechaFin = fechaEntrega)


        return redirect(reverse('listado_libros'))
        
    else:
        lugares = LugarPrestamo.objects.all()
        detalles_prestamo = Libro.objects.filter(pk=pk)
        return render(request, 'gestion/detalle_prestamo.html', {'lugares': lugares, 'detalles_prestamo': detalles_prestamo[0]})
    
        

class ProfileView(ListView):
    model = Prestamo
    template_name = 'prestamo_list.html'
    context_object_name = 'prestamos'
    paginate_by = 10

    def get_queryset(self):
        return Prestamo.objects.filter(usuario=self.request.user, entregado=False)

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('profile'))
        else:
            return render(request, 'gestion/login.html', { 'error' : "Usuario y/o contraseña incorrectos."})        
    else:        
        return render(request, 'gestion/login.html')
    

def register_view(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UsuarioForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return redirect(reverse('login'))
    else:
        uf = UserForm(prefix='user')
        upf = UsuarioForm(prefix='userprofile')
    return render(request,'gestion/registro.html', 
                                               dict(userform=uf,
                                                    userprofileform=upf),
                                               )        
        #return render(request, 'gestion/registro.html')

def remove_prestamo_view(request, pk):
    prestamo = Prestamo.objects.get(pk=pk)
    prestamo.entregado = True
    prestamo.save()
    return redirect(reverse('profile'))
