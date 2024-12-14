from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product

# Página principal
@login_required
def homepage(request):
    products = Product.objects.all()  # Obtiene todos los productos
    return render(request, 'ecommerce/home.html', {'products': products})

# Página de login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')  # Redirige a la página principal tras iniciar sesión
        else:
            messages.error(request, 'Credenciales incorrectas.')
    return render(request, 'ecommerce/login.html')

from django.contrib.auth import logout

# Vista para cerrar sesión
def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('login')  # Redirige al login
