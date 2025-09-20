from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy

class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, f'¡Bienvenido de vuelta, {form.get_user().username}!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Nombre de usuario o contraseña inválidos.')
        return super().form_invalid(form)

class RegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Registro exitoso! Por favor, inicia sesión.')
        return response

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')

def home_view(request):
    return render(request, 'home.html')
