from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Score(models.Model):
	highest_score = models.IntegerField(null=True, blank=True)
	total_questions = models.IntegerField(null=True, blank=True)
	current_score = models.IntegerField(null=True, blank=True)
	right_attempt = models.IntegerField(null=True, blank=True)
	wrong_attempt = models.IntegerField(null=True, blank=True)
	player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')



	class Meta:
		verbose_name_plural = 'Scores'

	def __str__(self):
		return "{}".format(self.player)