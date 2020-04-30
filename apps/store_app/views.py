from django.shortcuts import render, redirect, HttpResponse 
# Using Django Messages: https://docs.djangoproject.com/en/1.11/ref/contrib/messages/#displaying-messages 
from django.contrib import messages 
from .models import * 
from .forms import ProductForm
from django.views.generic import View
 
 
# Create your views here. 

class Products(View):
    def get(self, request):
        allProducts = Product.objects.all()

        context = {
            'prodForm' : ProductForm,
            'all_products' : allProducts,

        }

        return render(request, 'store_app/index.html', context)

    def post(self, request):
        

        # create new product here
        newProduct = Product.objects.create(name=request.POST['name'], desc=request.POST['desc'], brand=request.POST['brand'], price=request.POST['price'])

        allProducts = Product.objects.all()

        context = {
            'prodForm' : ProductForm,
            'all_products' : allProducts,
            'newProduct' : newProduct,

        }
        return render(request, 'store_app/index.html', context)

class ThisProduct(View):
    def get(self, request, id):
        allProducts = Product.objects.all()
        thisProduct = Product.objects.get(id=id)
        context = {
            'prodForm' : ProductForm,
            'all_products' : allProducts,
            'thisProduct' : thisProduct,

        }

        return render(request, 'store_app/thisProduct.html', context)

    def post(self, request, id):
        print('RUNNING THISPRODUCT.post')
        thisProduct = Product.objects.get(id=id)
        # update selected product here
        thisProduct.name = request.POST['name']
        thisProduct.desc = request.POST['desc']
        thisProduct.brand = request.POST['brand']
        thisProduct.price = request.POST['price']
        thisProduct.save()

        allProducts = Product.objects.all()

        context = {
            'prodForm' : ProductForm,
            'all_products' : allProducts,
            'thisProduct' : thisProduct,
        }
        return render(request, 'store_app/thisProduct.html', context)


def index(request): 
    
    allProducts = Product.objects.all()

    context = {
        'prodForm' : ProductForm,
        'all_products' : allProducts,


    }

    return render(request, 'store_app/index.html', context) 




def delete(request, id):
    thisProduct = Product.objects.get(id=id)
    thisProduct.delete()

    return redirect('/products/')
    









