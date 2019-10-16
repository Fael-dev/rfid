from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name='homepage'),
	path('lista/', views.listar, name='listar'),
	path('lista/delete/<int:id>', views.deleteObj, name='delete-teste'),
	path('lista/cadastro/<int:id>', views.add, name='add-objeto'),
	path('lista/historico/<str:code>', views.historico, name='historico'),
]