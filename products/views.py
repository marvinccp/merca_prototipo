from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.contrib import messages


def home(request):
    return render (request, 'products_templates/index.html', {})


def product_create(request):
    
    if request.method == 'GET':
        product_form = ProductForm()
        context = {
            'product_form': product_form,
        }
        return render(request, 'products_templates/product_create.html', context)
    
    if request.method == 'POST' and ProductForm:
        product_form = ProductForm(request.POST)
        if product_form.is_valid:
            product_form.save()
            
        return redirect('product_create') 
   

def category_create(request):

    if request.method == 'GET':
        category_form = CategoryForm()
        context = {
            'category_form': category_form
        }
        return render(request, 'products_templates/category_create.html', context)

    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid:
            category_form.save()

        return redirect('product_create')


def detail(request, id):
    product = Product.objects.get(id = id)
    context = {
        'product' : product
    }
    return render(request, 'products_templates/detail.html', context)


def category_detail(request, category):
    category = Category.objects.get(name = category)
    category_products = category.product_set.all()
    context = {
        'category':category,
        'category_products': category_products
    }
    return render(request, 'products_templates/category_detail.html', context)


def categories(request):
    
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products_templates/categories.html', context)


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('category_detail',  category = product.category)


def update(request, id):
    product = Product.objects.get(id = id)
    if(request.method == 'GET'):
        
        form = ProductForm(instance=product)
        context = {
            'form': form,
        }
        return render(request, 'products_templates/update.html', context)
    
    if(request.method == 'POST'):
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        messages.success(request, 'Actualizado con exito')
        return redirect('category_detail',  category=product.category)

