from django.db import models
from taggit.managers import TaggableManager
from simply_save.settings import AUTH_USER_MODEL


class Bookmark(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    url = models.URLField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    is_public = models.BooleanField(default=True)
    tags = TaggableManager()

    def __str__(self):
        return self.url
