from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Report(models.Model):
    title = models.CharField(max_length=100, default="Bad Roads", editable=True)
    location = models.CharField(max_length=100, default="Area", editable=True)
    slug = models.SlugField(max_length=50, default="")
    content = models.TextField(default="")
    date = models.DateTimeField(default=timezone.now)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.content[0:40] + "..."