import os
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_delete

class Member(models.Model):
	name = models.CharField(max_length=50)
	avatar = models.ImageField(upload_to='avatares/')
	job = models.CharField(max_length=50)
	resume = models.TextField()

	def __str__(self):
		return self.name

# Delete image if in admin panel we delete the entry
@receiver(pre_delete, sender=Member)
def photo_delete(sender, instance, **kwargs):
	# Lets build the path, removing /media/ from avatar.url
	# because MEDIA_ROOT already has /media/
	avatar_url = "/".join(instance.avatar.url.split("/")[2:])

	os.remove(os.path.join(settings.MEDIA_ROOT, avatar_url))