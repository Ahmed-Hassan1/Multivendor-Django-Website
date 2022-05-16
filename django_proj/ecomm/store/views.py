#Remove excess auth stuff

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product,CarouselBanner, SubCategory, Category

# Create your views here.

def homeView(request):
    #order product by date for the home page
    products = Product.objects.all()[:8]
    banners=CarouselBanner.objects.all()
    mainCats=Category.objects.all()
    context={'products':products,'banners':banners,'mainCats':mainCats}

    return render(request,'store/home.html',context)


def instrumentView(request,pk):
    subs=Category.objects.get(name=pk)
    subCats=SubCategory.objects.all().filter(category__name=subs)
    products= Product.objects.filter(category__name=subs)
    print(products)
    context = {'subCats':subCats,'products':products}

    return render(request,'store/instruments.html',context)

def subCatView(request,pk):
    subCat=SubCategory.objects.get(name=pk)
    products = Product.objects.filter(subCategory__name=subCat)
    print('Products:')
    print(products)
    context = {'products':products}
    print('SubCat:')
    print(subCat)
    return render(request,'store/subCat.html',context)    

def productView(request,pk):
    product=Product.objects.get(slug=pk)
    context={'product':product}
    return render(request,'store/product.html',context)

def oudView(request):
    if request.GET.get('filter_by')=='HighToLow':
        products = Product.objects.order_by('-price')
        context={'products':products}
        return render(request,'store/ouds.html',context)

    if request.GET.get('filter_by')=='LowToHigh':
        products = Product.objects.order_by('price')
        context={'products':products}
        return render(request,'store/ouds.html',context)
    
    products = Product.objects.all()
    context={'products':products}
    return render(request,'store/ouds.html',context)


