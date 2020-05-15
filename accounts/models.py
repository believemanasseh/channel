from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	# Additional attributes
	pass

	def __str__(self):
		return self.username

