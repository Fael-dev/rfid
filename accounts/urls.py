from django.urls import path
from . import views 


urlpatterns = [
	path('register/', views.register, name="signup"),
	path('recover/', views.recover, name='recover'),
	path('myaccount/', views.myaccount, name='myaccount')
]