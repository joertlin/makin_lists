from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import datetime

class check_lists(models.Model):
	"""
	This is the table that identifies lists that the user has generated.
	"""
	list_id = models.AutoField(primary_key=True)
	list_name = models.CharField(max_length = 10)
	date_created = models.DateTimeField('date list was created')
	date_completed = models.DateTimeField('date list was completed',null = True)
	user = models.ForeignKey(User)

	def is_a_complete_list(self):
		if self.date_completed == 'null':
			return False
		else:
			return True 



#class Question(models.Model):
#	question_text = models.CharField(max_length = 200)
#	pub_date = models.DateTimeField('date published')
#
#	def __str__(self):
#		return self.question_text
#
#	def was_published_recently(self):
#		now = timezone.now()
#		return now - datetime.timedelta(days = 1) <= self.pub_date <= now
#
#	was_published_recently.admin_order_field = 'pub_date'
#	was_published_recently.boolean = True
#	was_published_recently.short_description = 'Published recently?'
#
#class Choice(models.Model):
#	question = models.ForeignKey(Question)
#	choice_text = models.CharField(max_length = 200)
#	votes = models.IntegerField(default = 0)
#
#	def __str__(self):
#		return self.choice_text