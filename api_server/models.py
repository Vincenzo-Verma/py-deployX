from django.db import models
import uuid

# Create your models here.

class user(models.Model):
    id = models.UUIDField( primary_key = True, default = uuid.uuid64, editable = False )