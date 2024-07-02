from django.shortcuts import render, redirect
from .models import Autos
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def autos(request):
    autos = Autos.objects.all()
    return render(request, "autos/autos.html", {

        "autos":autos

    })

def exit(request):
    logout(request)
    return redirect('index')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            username = user_creation_form.cleaned_data['username']
            password = user_creation_form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
        else:
            messages.error(request, "Formulario inválido. Por favor, corrige los errores.")

    return render(request, 'registration/register.html', data)

def descripcion (request, id_auto):
    autos = Autos.objects.all(id=id_auto)
    return render(request, 'descripciones/descripcion.html', {

        "autos":autos

    })