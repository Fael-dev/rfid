from django.db import models
from datetime import datetime

class Objeto(models.Model):
	server = models.CharField(max_length=15)
	antena = models.CharField(max_length=10)
	date = models.DateTimeField(default=datetime.now)
	code = models.TextField()
	objeto = models.CharField(max_length=100)

	def data_hora(self):
		self.date = datetime.now()
		self.save()

	def __str__(self):
		return self.objeto

class Historico(models.Model):
	server = models.CharField(max_length=15)
	antena = models.CharField(max_length=10)
	date = models.DateTimeField(default=datetime.now)
	code = models.TextField()
	objeto = models.CharField(max_length=100)

	def data_hora(self):
		self.date = datetime.now()
		self.save()

	def __str__(self):
		return self.objeto
	

