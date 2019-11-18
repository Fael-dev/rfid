from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#from django.urls import reverse_lazy 
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random



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
            us = User.objects.get(email=mail)
            dados = 'aEiOu0123456789'
            new_senha = "".join(random.sample(dados, len(dados)))
            us.set_password(new_senha)
            us.save()
            email = us.email
            #ENVIAR A SENHA PARA EMAIL E INFORMAR AO USUÁRIO 
            msg = 'Sua nova senha na Aironnet é: '+new_senha
            send_mail('Recuperação de senha.',msg, settings.EMAIL_HOST_USER, [email,], fail_silently=False)
            messages.success(request, 'Foi enviada uma nova senha para seu email cadastrado.')
            return redirect('/accounts/login')
        else:
            #INFORMAR QUE O EMAIL É INVÁLIDO
            messages.warning(request, 'Email inválido!')
            return redirect('/accounts/login')
    else:
        return redirect('/accounts/login')

# Testando envio de emails via console, pois porta 587 provavelmente bloqueada

def myaccount(request):
    template_name = 'myaccount.html'
    return render(request, template_name)
