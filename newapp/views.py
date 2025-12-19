from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

def say_hello(request):
    #query_set = Product.objects.all()

    #Iterating over the query_set to generate SQL code to send to the database
    # for product in query_set:
    #     print(product)

    #get() method
    # product = Product.objects.get(pk=1)

    queryset = Product.objects.filter(unit_price__range = (20,30))

    return render(request,'index.html',{'name' : 'lemon','products': list(queryset)})
