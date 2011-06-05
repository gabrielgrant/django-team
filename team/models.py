from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from static_filtered_images.fields import FilteredImageField
from static_filtered_images.image_filters import ResizeFilter


class Team(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name

class Member(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, related_name='team_profile', )
	name = models.CharField(max_length=200)
	title = models.CharField(max_length=200, blank=True)
	join_date = models.DateField()
	bio = models.TextField(blank=True)
	image = models.ImageField(upload_to='team_images', blank=True)
	display_image = FilteredImageField(max_length=200,
		src_field=image,
		filter_chain=[
			ResizeFilter(**settings.TEAM_IMAGE_RESIZE),
		]
	)
	teams = models.ManyToManyField(Team, related_name='members')
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.name
