from operator import mod
from django.db import models
from store.models import Product
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.models import GenericForeignKey 
# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tags to applied to what object
    tag = models.ForeignKey(Tag , on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType , on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    contnet_object = GenericForeignKey()