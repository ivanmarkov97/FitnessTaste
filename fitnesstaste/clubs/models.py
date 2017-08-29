from django.db import models

# Create your models here.
class Club(models.Model):
	club_name = models.CharField(max_length = 80)
	club_adrees = models.CharField(max_length = 160)
	club_contact = models.CharField(max_length = 80)
	club_email = models.CharField(max_length = 80)
	club_description = models.TextField()

	def __str__(self):
		return self.club_name