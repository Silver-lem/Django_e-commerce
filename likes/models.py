from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class LikedItem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #If a user is deleted then all the objects( that the user has liked )related to the user must be deleted
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    current_object = GenericForeignKey()