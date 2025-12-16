from django.db import models
#from store import Product
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    #Using this class we can find our what tag is appleid to what object
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
#When we delete a tag we need to delete it form all the associated objects

#Identifying the object this tag is appleid to

#POOR WAY
    #product = models.ForeignKey(Product)#the tags app depends on the store app
#which is not ideal

#A generic way to identify an object we need two pieces of info 1. Type(product,video,article...) 2. ID of the object
#Using these two pieces of info we can identify any object in our application in db terms we can identify any record in any tables
#Since using type we can find table using id we can find the record.

#So instead of using a concrete model like product we need to use an abstract model like ContentType which comes with django
# In the list of apps an app called contenttypes is pre-defined. 
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()#every table is going to have a primary key and all primary keys are positive integer.
#limitation of this solution is if primary key is not an integer


#When querying data we might get the actual onject that this tag is appplying to
    content_object = GenericForeignKey()
#Content object can now read the particular object that a particular tag is applied to

