from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from django.urls import reverse_lazy 
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail


def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('/accounts/register')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'registration/register.html', {'form': f})
'''
class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/register.html'
'''


def recover(request):
    mail = request.POST.get('email')
    if request.method == 'POST':
        user = User.objects.filter(email=mail)
        if user:
            #ENVIAR A SENHA PARA EMAIL E INFORMAR AO USUÁRIO
            #send_mail('Subject', 'Senha a enviar', 'hlysa697i@brymstonne.org', ['44eff3cd68@emailcu.icu',])
            messages.success(request, 'Senha enviada para seu email.')
            return redirect('/accounts/login')
        else:
            #INFORMAR QUE O EMAIL É INVÁLIDO
            messages.info(request, 'Email inválido!')
            return redirect('/accounts/login')
    else:
        return redirect('/accounts/login')

    