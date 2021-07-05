from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255, blank=False, null=False)
	description = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)

	class Meta():
		ordering = ('complete', )

	def __str__(self):
		return self.title

	def created_pretty(self):
		return self.created.strftime('%I:%M %p, %A %B %Y')

	def summary(self):
		return self.description[:50]