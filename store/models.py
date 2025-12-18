from django.db import models

#For Django Field Types : https://docs.djangoproject.com/en/6.0/ref/models/fields/

#MANY - TO MANY Relationship
class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    #by default product_set is created by django to change it use related_name = ''

#ONE-TO-MANY Relationship
class Collection(models.Model):#A collection can have multiple products
    title = models.CharField(max_length = 255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True , related_name= '+')

#Product class
class Product(models.Model):
    title = models.CharField(max_length = 255) #varchar(255)
    slug = models.SlugField()#made this change after 1 migration 
    description = models.TextField()
    #for example max price is 9999.99
    unit_price = models.DecimalField(max_digits = 6,decimal_places = 2) #FloatFeild can cause rounding issues
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now = True) #auto_now_add

    #Establishing a One to many relation
    collection = models.ForeignKey(Collection,on_delete=models.PROTECT)#When you delete a collection we do no to delete all the products in the collection
#When it is no possible to maintain the Parent class above the Child class the pass the parent class as a string 
#In this case collection = models.ForeignKey('Collection') and so on.

#Establishing a many to many relationship
    promotions = models.ManyToManyField(Promotion)



#Customer class
class Customer(models.Model):
    MEMBERSHIP_BRONZE  = 'B'#Defining a new attribute seperately to allow future modification
    MEMBERSHIP_SILVER  = 'S'
    MEMBERSHIP_GOLD  = 'G'
    
    # MEMBERSHIP_CHOICES = [
    #     (MEMBERSHIP_BRONZE , 'Bronze'),#Instead of having('B' , 'Bronze)
    #     ('S' , 'Silver'),
    #     ('G' , 'Gold'),
    # ]
    #To maintain consistency create attricbutes for all choices

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE , 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True) #To not have duplicate emails
    phone = models.CharField(max_length = 255)
    birth_date = models.DateField(null = True)#birth_date is an instance of datefield which is nullable
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICES , default = MEMBERSHIP_BRONZE) 

#Deleting--here committing for the prupose of deleting migrations
    # #Adding Metadata
    # class Meta:
    #     db_table = 'store_customers'#not recommended but now just understanding metadata
    #     indexes = [
    #         models.Index(fields=['last_name','first_name'])
    #     ]

#Order class with 2 fields - placed_at and payments statt
class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE= 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING,'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED,'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)#auto-populated at the time the object is created
    payment_status = models.CharField(max_length=1,choices = PAYMENT_STATUS_CHOICES , default = PAYMENT_STATUS_PENDING)
#Relationship establishing
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class OrderItem(models.Model):#An Order can have multiple items
    order = models.ForeignKey(Order,on_delete=models.PROTECT)#When an order is deleted then orderitem is not deleted
    product = models.ForeignKey(Product,on_delete=models.PROTECT)#deleting a product does not delete the associated orderitems
    quantity = models.PositiveSmallIntegerField()#preventing negative values to be stored
    unit_price = models.DecimalField(max_digits = 6,decimal_places = 2)#already exists in product class so why is it defined...since the price can change over time


#DEFINING A ONE-TO-ONE RELATIONSHIP
#Address class
class Address(models.Model):#Each customer has one address and each adress can correspond to only one customer
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
#In this relationship the Customer is the Parent and address is the child --Customer should exist for an address to exist
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key = True)
#If customer is not a primary key,django creates an ID for each address so every addres will have an id and there will be a one-to-many relationships with the customers and addresses.
# Since many addresses can exist with the same customer

#should we define a reverse relationship in the customer class...should an address field exist in class customer for the reverse relationship no since django does it automatically.
 
#Adress class as a ONE - TO - MANY RELATION
#Address class
# class Address(models.Model):#Each customer can have multiple addresses
#     street = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class Cart(models.Model):#A cart can have multiple items
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)#If you delete a cart we should delete the items in the cart
    product = models.ForeignKey(Product,on_delete=models.CASCADE)#deleting a product meaning the product has never been ordered before it must be removed from all existing shopping carts
    quantity = models.PositiveSmallIntegerField()




