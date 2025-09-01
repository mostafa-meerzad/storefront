from django.db import models
from store.models import Product
# this is the poor way of implementing relationship between TaggedItem and Product
# what if tomorrow we want to tag articles or videos
# this way "tags" app is dependant on the "store" app
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag applied to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # the poor way of implementing
    # product = models.ForeignKey(Product )
    #
    #  we need to identify a generic-object
    #  to do that we need two pieces of information
    # 1 Type (product, video, article)
    # 2 ID
    # using these two pieces of information we can identify any object in our application
    # using Type we can find the table and using ID we can find the record
    #
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
