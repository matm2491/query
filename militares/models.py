from django.db import models


		

class Cuartel (models.Model):
	nombre    = models.CharField(max_length=80)
	ubicacion = models.CharField(max_length=160)
	
	
	class Meta:
		db_table = 'sm_cuartel'

	def __str__(self):
		return "%s" % (self.nombre)
		


class Soldado(models.Model):
	primer_nombre    = models.CharField(max_length=50)
	segundo_nombre   = models.CharField(max_length=50)
	primer_apellido  = models.CharField(max_length=50)
	segundo_apellido = models.CharField(max_length=50)
	cedula           = models.IntegerField(max_length=20)
	graduacion       = models.DateTimeField('date published')
	cuartel          = models.ForeignKey(Cuartel, on_delete=models.CASCADE)
	class Meta:
		db_table = 'sm_soldados'

	def __str__(self):
		return "%s" % (self.primer_nombre)
	
class Servicio (models.Model):
	nombre      = models.CharField(max_length=80)
	descripcion = models.CharField(max_length=300)
	
	class Meta:
		db_table = 'sm_servicios'

	def __str__(self):
		return "%s %s" % (self.nombre, self.descripcion)
		

class Cuerpos_del_ejercito (models.Model):
	denominacion = models.CharField(max_length=80)

	class Meta:
		db_table = 'sm_cuerpos_del_ejercito'

	def __str__(self):
		return "%s" % (self.denominacion)
		

class Compañia (models.Model):
	numero_compania = models.CharField(max_length=80)
	actividad       = models.CharField(max_length=80)

	class Meta:
		db_table = 'sm_compañias'

	def __str__(self):
		return "%s" % (self.numero_compania)
		

class Soldados_registrado(models.Model):
	soldado  = models.ForeignKey(Soldado, on_delete=models.CASCADE)
	cuartel  = models.ForeignKey(Cuartel, on_delete=models.CASCADE)
	servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
	cuerpo   = models.ForeignKey(Cuerpos_del_ejercito, on_delete=models.CASCADE)
	compania = models.ForeignKey(Compañia, on_delete=models.CASCADE)
	

	class Meta:
		db_table = 'sm_soldados_registrados'
		



