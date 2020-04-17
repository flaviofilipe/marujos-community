from django.conf import settings
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='images/posts/')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_image(self):
        return self.image.url