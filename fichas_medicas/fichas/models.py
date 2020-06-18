from django.db import models


# Create your models here.
class Paciente(models.Model):
	fullname = models.CharField(max_length=100)
	email	 = models.CharField(max_length=100)

	def __str__(self):
		return self.fullname

class Ficha(models.Model):
	number = models.IntegerField()
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
	descripcion = models.CharField(max_length=100)
	fecha = models.DateField(auto_now=True, editable=True)
   	
