from django.db import models
from .utils import default_expiry

# Create your models here.

class StorageModel(models.Model):
    file_id = models.IntegerField(primary_key=True)
    file = models.FileField()
    uploaded_time = models.DateTimeField(auto_now_add=True)
    expires_on = models.DateTimeField(default=default_expiry)
    url = models.URLField(blank=True)
    file_path = models.CharField(max_length=100)  #filepathfield

    def __str__(self):
        return self.file.name
