from django.db import models

# Create your models here.
class Service(models.Model):
	service_name = models.CharField(max_length = 80)
	service_image = models.ImageField(upload_to = 'services_images')
	service_secription = models.TextField()

	def __str__(self):
		return self.service_name