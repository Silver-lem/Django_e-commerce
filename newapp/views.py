from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q,F,Func,Value
from store.models import Product,Customer,Collection,Order,OrderItem
from django.db.models.functions import Concat

def say_hello(request):
    #query_set = Product.objects.all()

    #Iterating over the query_set to generate SQL code to send to the database
    # for product in query_set:
    #     print(product)

    #get() method
    # product = Product.objects.get(pk=1)
    
    # Complex Lookups Using Q objects
    # queryset = Product.objects.filter(inventory__lt = 10 , unit_price__lt = 20)
    # queryset = Product.objects.filter(inventory__lt = 10 ).filter(unit_price__lt = 20)
    # queryset = Product.objects.filter(Q(inventory__lt = 10) | ~Q(unit_price__lt = 20))

    #Referencing Objects - comparing two fields
    # queryset = Product.objects.filter(inventory = F('unit_price'))

    #Sorting
    # queryset = Product.objects.order_by('unit_price','-title')
    # queryset = Product.objects.order_by('-title')
    # queryset = Product.objects.order_by('-title').reverse()
    
    # product = Product.objects.order_by('unit_price')[0] 
    # - Trying to access just one element/item
    # so instead of 'products': list(queryset) we pass 'product' : product

    #An Alternate way of doing the above is
    # product = Product.objects.earliest('unit_price') - to get the first item when sorted
    # product = Product.objects.latest('unit_price') - the last item 

    #Limiting Results
    # queryset = Product.objects.all()[:5]
    # queryset = Product.objects.all()[5:10]

    # Filtering Objects 
        # Products whose price is between 20 - 30
        #Customers with .com accounts
        # queryset = Customer.objects.filter(email__icontains = '.com')
        #Collections that don't have a featured product
        # queryset = Collection.objects.filter(featured_product__isnull=True)
        #Products with low inventory(less than 10)
        # queryset = Product.objects.filter(inventory__lt = 10)
        #Orders placed by custimer with id = 1
        # queryset = Order.objects.filter(customer__id=1)
        #order items for products in collection
        # queryset = OrderItem.objects.filter(Product__collection__id=3)

    # Selecting Field to query
    # queryset = Product.objects.values('id' , 'title') - gives dictionaries
    # queryset = Product.objects.values_list('id' , 'title')

    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = Product.objects.only('id' , 'title')

    # Selecting Related Objects
    # queryset = Product.objects.all()

    #Annotating objects - to add additional attributed before querying them
    # queryset = Customer.objects.annotate(is_new=True) -- TypeError : received non-expression
    # queryset = Customer.objects.annotate(new_id=F('id'))

    queryset = Customer.objects.annotate(
        #CONCAT function of a db engine
        full_name=Func(F('first_name'),Value(' '),F('last_name'), function='CONCAT')
        ) 
    
    queryset = Customer.objects.annotate(
        #CONCAT function of a db engine
        full_name=Concat('first_name',Value(' '),'last_name')
        ) 
    # return render(request,'index.html',{'name' : 'lemon','products': list(queryset)})
    return render(request,'index.html',{'name' : 'lemon','result': list(queryset)})
    # return render(request,'index.html',{'name' : 'lemon','product': product}) #we must also change the template to accomodate this change
