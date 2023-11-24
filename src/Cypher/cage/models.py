from django.db import models

class Count(models.Model):
	visited = models.BooleanField(default=False)

