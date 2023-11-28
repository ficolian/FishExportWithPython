from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list" : queryset
    }
    # form = ProductForm(request.POST or None)
    # print (form.errors)
    # if form.is_valid():
    #     form.save()
    #     form = ProductForm()
    return render(request, "products/product_list.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    print (form.errors)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    # if (request.POST):
    #     print('go to list')
    #     product_list_view(request)
    # else:
    return render(request, "products/product_create.html", context)

def dynamic_look_up(request, id):
    obj = get_object_or_404(Product, id = id)
    try:
        obj = Product.objects.get(id=id)
    except Product.DoestNotExist:
        raise Http404
    
    context = {
        "object" : obj
    }
    return render (request, "products/product_detail.html",context)

def render_initial_data(request):
    initial_data = {
        'title':"My good",
        'description' :"this"
    }
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance =obj)
    context = {
        'form' : form
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)
    
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id = id)
    if request.method == 'POST':
        obj.delete()

    context = {
        "object": obj
    }
    return render (request, "products/product_delete.html", context)